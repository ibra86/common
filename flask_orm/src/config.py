import os


class Config:
    SECRET_KEY = 'very_secret_key'
    PG_USER = "aibragimov"
    PG_PASSWORD = "password"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "flask_practice"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


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
