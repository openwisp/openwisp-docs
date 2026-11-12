import os
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from reportlab.pdfgen import canvas


class PdfCheckTests(unittest.TestCase):
    """Run the build validation script with unrelated commands stubbed.

    Valid PDFs pass to link validation; broken PDFs must fail beforehand.
    """

    def test_qa_rejects_broken_pdfs(self):
        script = Path(__file__).resolve().parent.parent / "run-build-checks"
        for broken in [False, True]:
            with self.subTest(broken=broken), TemporaryDirectory() as directory:
                root = Path(directory)
                bin_dir = root / "bin"
                bin_dir.mkdir()
                for command in [
                    "sleep",
                ]:
                    stub = bin_dir / command
                    stub.write_text("#!/bin/sh\nexit 0\n")
                    stub.chmod(0o755)
                build_dir = root / "_build"
                build_dir.mkdir()
                link_check = bin_dir / "pylinkvalidate.py"
                link_check.write_text('#!/bin/sh\ntouch "$LINK_CHECK_MARKER"\n')
                link_check.chmod(0o755)
                python = bin_dir / "python"
                python.write_text(
                    '#!/bin/sh\nif [ "$1" = "-m" ]; then exec /usr/bin/sleep 60; fi\n'
                )
                python.chmod(0o755)
                pdf = build_dir / "valid file.pdf"
                document = canvas.Canvas(str(pdf))
                document.drawString(100, 700, "Valid PDF")
                document.save()
                if broken:
                    (build_dir / "broken file.pdf").touch()
                result = subprocess.run(
                    [str(script)],
                    cwd=root,
                    env={
                        **os.environ,
                        "PATH": f'{bin_dir}:{os.environ["PATH"]}',
                        "LINK_CHECK_MARKER": str(root / "link-checked"),
                    },
                    capture_output=True,
                    text=True,
                    timeout=15,
                )
                if broken:
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertIn("broken file.pdf is broken", result.stdout)
                    self.assertFalse((root / "link-checked").exists())
                else:
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertTrue((root / "link-checked").exists())
