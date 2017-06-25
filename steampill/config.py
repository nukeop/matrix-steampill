import json
import os

config_path = os.path.join(os.getcwd(), 'config.json')
config = json.loads(''.join(open(config_path, 'r').readlines()))

def reload_config():
    config = json.loads(''.join(open(config_path, 'r').readlines()))
