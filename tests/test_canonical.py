import json
import os
import runpy
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import mock_open, patch

from jinja2 import ChoiceLoader, DictLoader, Environment, FileSystemLoader

import build
from version_switcher.event_callbacks import set_version_context


class CanonicalTests(unittest.TestCase):
    def test_canonical_is_omitted_without_context(self):
        env = Environment(
            loader=ChoiceLoader(
                [
                    DictLoader({"!layout.html": "{% block linktags %}{% endblock %}"}),
                    FileSystemLoader(Path(__file__).parent.parent / "_templates"),
                ]
            )
        )
        html = env.get_template("layout.html").render()
        self.assertNotIn('rel="canonical"', html)

    def test_stable_alias_is_replaced(self):
        with TemporaryDirectory() as temporary_directory:
            build_dir = Path(temporary_directory)
            stable_alias = build_dir / "stable"
            for version in ["25.10", "26.09"]:
                version_dir = build_dir / version
                version_dir.mkdir()
                build.create_stable_alias(build_dir, version)
                self.assertEqual(stable_alias.resolve(), version_dir)

    def test_stable_alias_failure_is_propagated(self):
        error = subprocess.CalledProcessError(1, ["ln"])
        with (
            TemporaryDirectory() as temporary_directory,
            patch.object(build.subprocess, "run", side_effect=error),
        ):
            with self.assertRaisesRegex(subprocess.CalledProcessError, "ln"):
                build.create_stable_alias(temporary_directory, "26.09")

    def test_notfound_urls_prefix_uses_current_version(self):
        with patch.dict(
            os.environ, {"OPENWISP2_VERSION": "22.05", "DOCS_ROOT": "/docs"}
        ):
            config = runpy.run_path("conf.py")
        self.assertEqual(config["notfound_urls_prefix"], "/docs/22.05/")

    def test_rendered_canonical(self):
        env = Environment(
            loader=ChoiceLoader(
                [
                    DictLoader({"!layout.html": "{% block linktags %}{% endblock %}"}),
                    FileSystemLoader(Path(__file__).parent.parent / "_templates"),
                ]
            )
        )
        cases = [
            ("26.09", "user/example", ["26.09"], "stable/user/example.html"),
            ("22.05", "user/example", ["22.05", "26.09"], "stable/user/example.html"),
            ("22.05", "user/removed", ["22.05"], "22.05/user/removed.html"),
            ("dev", "user/example", ["dev", "26.09"], "stable/user/example.html"),
            ("26.09", "index", ["26.09"], "stable/"),
            ("22.05", "user/index", ["22.05", "26.09"], "stable/user/"),
            ("22.05", "old/index", ["22.05"], "22.05/old/"),
            ("dev", "index", ["dev", "26.09"], "stable/"),
            ("26.09", "search", ["dev", "26.09"], "stable/search.html"),
            ("22.05", "search", ["dev", "26.09"], "stable/search.html"),
            ("dev", "user/new", ["dev"], "dev/user/new.html"),
            ("dev", "user/index", ["dev", "26.09"], "stable/user/"),
            ("26.09", "security/index", ["dev", "26.09"], "dev/security/"),
            (
                "22.05",
                "security/disclosing-vulnerabilities",
                ["dev", "22.05", "26.09"],
                "dev/security/disclosing-vulnerabilities.html",
            ),
            (
                "dev",
                "security/future-policy",
                ["dev"],
                "dev/security/future-policy.html",
            ),
            (
                "22.05",
                "general/code-of-conduct",
                ["dev", "22.05", "26.09"],
                "dev/general/code-of-conduct.html",
            ),
            (
                "26.09",
                "developer/contributing",
                ["dev", "26.09"],
                "dev/developer/contributing.html",
            ),
            (
                "22.05",
                "security-extra/example",
                ["22.05", "26.09"],
                "stable/security-extra/example.html",
            ),
        ]
        for version, page, versions, expected in cases:
            with self.subTest(version=version, page=page):
                app = SimpleNamespace(
                    builder=SimpleNamespace(
                        name="html",
                        _ow_version_map={page: versions} if versions else {},
                    )
                )
                context = {
                    "current_ow_version": version,
                    "stable_version": "26.09",
                    "ow_versions": [],
                    "html_baseurl": "https://openwisp.io",
                    "docs_root": "/docs",
                    "pagename": page,
                }
                set_version_context(app, page, None, context, None)
                html = env.get_template("layout.html").render(context)
                self.assertIn(
                    f'<link rel="canonical" href="https://openwisp.io/docs/{expected}"',
                    html,
                )
                self.assertEqual(html.count('rel="canonical"'), 1)

    def test_partial_build_stable_version(self):
        config = {
            "modules": [],
            "versions": [{"name": name} for name in ["dev", "26.09", "22.05"]],
        }
        for selected in ["dev", "22.05", "26.09", None]:
            with self.subTest(selected=selected):
                argv = ["build.py", "--formats", "html"]
                if selected:
                    argv.extend(["--version", selected])
                with (
                    patch("sys.argv", argv),
                    patch("builtins.open", mock_open(read_data=json.dumps(config))),
                    patch.object(build, "clone_or_update_repo"),
                    patch.object(build.subprocess, "run") as run,
                ):
                    build.main()
                commands = run.call_args_list
                for call in commands:
                    if call.args[0][0] == "make":
                        self.assertEqual(call.kwargs["env"]["STABLE_VERSION"], "26.09")
                aliases = [call for call in commands if call.args[0][0] == "ln"]
                self.assertEqual(len(aliases), int(selected in [None, "26.09"]))
                if aliases:
                    self.assertEqual(aliases[0].args[0][1], "-rsfT")


if __name__ == "__main__":
    unittest.main()
