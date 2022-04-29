import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

mongoEngineConfig = {
    'db': 'roomie',
    'host': os.getenv('DATABASE_HOST'),
    'port': os.getenv('DATATBASE_PORT')
}
