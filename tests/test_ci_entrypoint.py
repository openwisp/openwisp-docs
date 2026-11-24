"""Check the test entry point without running the documentation suite."""

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class CiEntrypointTests(unittest.TestCase):
    def run_script(self, *arguments, status=0):
        with tempfile.TemporaryDirectory() as directory:
            fake = Path(directory) / "python"
            fake.write_text('#!/bin/sh\nprintf "%s\\n" "$@"\nexit "$STATUS"\n')
            fake.chmod(0o755)
            return subprocess.run(
                [str(ROOT / "runtests"), *arguments],
                cwd=ROOT,
                env={
                    **os.environ,
                    "PATH": f"{directory}:{os.environ['PATH']}",
                    "STATUS": str(status),
                },
                capture_output=True,
                text=True,
            )

    def test_default_discovery(self):
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout.splitlines(), ["-m", "unittest", "discover", "tests"]
        )

    def test_selected_file_and_safe_flag(self):
        result = self.run_script("-v", "tests/test_canonical.py")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout.splitlines(),
            [
                "-m",
                "unittest",
                "discover",
                "-s",
                "tests",
                "-p",
                "test_canonical.py",
                "-v",
            ],
        )

    def test_rejects_unsupported_arguments(self):
        for argument in ("--locals", "../test.py", "tests/test_x.py;id", "--"):
            with self.subTest(argument=argument):
                result = self.run_script(argument)
                self.assertEqual(result.returncode, 2)
                self.assertIn("unsupported", result.stderr.lower())
                self.assertEqual(result.stdout, "")

    def test_returns_runner_status(self):
        self.assertEqual(
            self.run_script("tests/test_canonical.py", status=17).returncode, 17
        )
