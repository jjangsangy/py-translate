import os
import json
import logging.config

def setup_logging(
    default_path=os.path.join('static', 'config.json'),
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as config:
            ini = json.load(config)['logger']
        logging.config.dictConfig(ini)
    else:
        logging.basicConfig(level=default_level)
