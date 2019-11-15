import os


class Config:
    pass


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
