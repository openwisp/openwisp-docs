from sphinx.builders.dummy import DummyBuilder
import json
from .utils import load_versions_map, VERSION_MAP_FILE


class VersionSwitcherIndexBuilder(DummyBuilder):
    """
    This custom builder is a subclass of the built-in `DummyBuilder` class.
    The `DummyBuilder` iterates over all the source files but it does not create
    any output files. It is used specifically to create the `VERSION_MAP_FILE`
    which is used for showing only relevant versions for each page in the
    version switcher.
    """

    name = 'version_map'

    def init(self):
        super().init()
        self.ow_version_map = load_versions_map()

    def finish(self):
        super().finish()
        with open(VERSION_MAP_FILE, 'w') as file:
            json.dump(self.ow_version_map, file)
