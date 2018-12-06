import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    SECRET_KEY = os.urandom(64)
    WTF_CSRF_ENABLED = True
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "secret"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {"Development": DevelopmentConfig, "Production": ProductionConfig}
