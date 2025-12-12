import yaml
import os
from box import ConfigBox


def read_yaml(path: os.path):
    with open(path, "r") as yaml_file:
        _yaml = yaml.safe_load(yaml_file)
        return ConfigBox(_yaml)
