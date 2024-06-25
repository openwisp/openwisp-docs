from sphinx.builders.dummy import DummyBuilder
import json
from .utils import load_versions_map, VERSION_MAP_FILE


class OpenwispDummyBuilder(DummyBuilder):
    name = 'ow_dummy'

    def init(self):
        super().init()
        self.ow_version_map = load_versions_map()

    def finish(self):
        super().finish()
        with open(VERSION_MAP_FILE, 'w') as file:
            json.dump(self.ow_version_map, file)
