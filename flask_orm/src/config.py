import os

from flask_restful.utils.crypto import encrypt


class Config:
    DATABASE = {
        "database": "flask_practice",
        "user": "aibragimov",
        "password": encrypt("dmVyeV9zZWNyZXRfcGFzc3dvcmQ=")
    }


class TestConfig(Config):
    pass


class ProductionConfig(Config):
    pass


def run_config():
    env = os.environ.get('ENV')
    if env == 'TEST':
        return TestConfig
    elif env == 'PROD':
        return ProductionConfig
    else:
        return Config
