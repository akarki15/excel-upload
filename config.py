""" Stores settings for the app """
DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEMERE = os.path.join(BASE_DIR, 'demere')
STATIC = os.path.join(DEMERE, 'static')
INPUT_FILE = os.path.join(STATIC, 'movies.csv')
OUTPUT_FILE = os.path.join(STATIC, 'dump')


# database configuration
DATABASE = os.path.join(BASE_DIR, 'demere.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'