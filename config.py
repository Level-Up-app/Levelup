from dotenv import load_dotenv
from pathlib import Path
from os import environ, path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Configuration from environment variables."""

    FLASK_ENV = environ.get("FLASK_ENV")
    FLASK_APP="run.py"
    
    # Statement for enabling the development environment 
    DEBUG = True

    # Specifying host and port for our server
    HOST = '127.0.0.1'
    PORT = 5000

    # Defining database that are working with
    MONGODB_SETTINGS = {
                        'db': 'levelup_db', 
                        'host': environ.get('MONGO_URI'),
                        'connect': True
                        }

    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')