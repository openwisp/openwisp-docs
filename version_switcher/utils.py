import json

VERSION_MAP_FILE = 'versions_map.json'


def load_versions_map():
    try:
        with open(VERSION_MAP_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
