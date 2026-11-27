"""Check installer phase selection without modifying the host."""

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class CiInstallerTests(unittest.TestCase):
    def run_script(self, **variables):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            log = path / "calls"
            for name in ("sudo", "python"):
                command = path / name
                command.write_text(
                    f'#!/bin/sh\nprintf "%s\\n" "{name} $*" >> "$CALLS"\n'
                    f'[ "${{FAIL_MATCH:-}}" != "{name} $*" ] || exit 17\n'
                )
                command.chmod(0o755)
            env = os.environ.copy()
            env.pop("CI_SYSTEM_DEPS_ONLY", None)
            env.pop("CI_SYSTEM_DEPS_READY", None)
            env.update(PATH=f"{path}:{env['PATH']}", CALLS=str(log), **variables)
            result = subprocess.run(
                [str(ROOT / "install-ci-deps.sh")],
                cwd=ROOT,
                env=env,
                capture_output=True,
                text=True,
            )
            return result, log.read_text().splitlines()

    def test_system_phase_only_installs_system_dependencies(self):
        result, calls = self.run_script(CI_SYSTEM_DEPS_ONLY="1")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            calls,
            [
                "sudo apt update",
                "sudo apt install -y libcairo2-dev poppler-utils",
                "sudo npm install -g prettier",
            ],
        )

    def test_reviewer_phase_only_installs_python_dependencies(self):
        result, calls = self.run_script(CI_SYSTEM_DEPS_READY="1")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            calls,
            [
                "python -m pip install -U pip wheel setuptools",
                "python -m pip install -U -r requirements.txt",
            ],
        )

    def test_default_installs_both_phases(self):
        result, calls = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            calls,
            [
                "sudo apt update",
                "sudo apt install -y libcairo2-dev poppler-utils",
                "sudo npm install -g prettier",
                "python -m pip install -U pip wheel setuptools",
                "python -m pip install -U -r requirements.txt",
            ],
        )

    def test_failures_stop_later_commands(self):
        for command in (
            "sudo apt install -y libcairo2-dev poppler-utils",
            "python -m pip install -U pip wheel setuptools",
        ):
            with self.subTest(command=command):
                result, calls = self.run_script(FAIL_MATCH=command)
                self.assertEqual(result.returncode, 17)
                self.assertEqual(calls[-1], command)
