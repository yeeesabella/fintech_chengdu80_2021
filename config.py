import configparser
from sqlalchemy import create_engine
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_DIR = os.path.join(ROOT_DIR, 'config.txt')

config = configparser.ConfigParser()
config.read(CONFIG_DIR)

engine = create_engine(config.get('database', 'con'))