import os
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


class QaCheckTests(unittest.TestCase):
    def test_checks_json_and_rst_without_python_docstrings(self):
        script = Path(__file__).resolve().parent.parent / "run-qa-checks"
        with TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            bin_dir = root / "bin"
            bin_dir.mkdir()
            qa_check = bin_dir / "openwisp-qa-check"
            qa_check.write_text("#!/bin/sh\nexit 0\n")
            qa_check.chmod(0o755)
            (root / "sort_spelling_wordlist.py").touch()
            json_file = root / "example.json"
            rst_file = root / "example.rst"
            (root / "example.py").write_text(
                '"""An unformatted Python docstring.  """\n'
            )
            env = {**os.environ, "PATH": f'{bin_dir}:{os.environ["PATH"]}'}

            json_file.write_text('{"a":1}\n')
            rst_file.write_text("Title\n=====\n")
            result = subprocess.run(
                [str(script)], cwd=root, env=env, capture_output=True
            )
            self.assertNotEqual(result.returncode, 0)

            json_file.write_text('{ "a": 1 }\n')
            rst_file.write_text(
                "Title\n=====\n\nThis line has trailing whitespace.   \n"
            )
            result = subprocess.run(
                [str(script)], cwd=root, env=env, capture_output=True
            )
            self.assertNotEqual(result.returncode, 0)

            rst_file.write_text("Title\n=====\n")
            result = subprocess.run(
                [str(script)], cwd=root, env=env, capture_output=True
            )
            self.assertEqual(result.returncode, 0, result.stderr.decode())
