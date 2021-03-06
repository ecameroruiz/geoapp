"""Flask Configuration"""

from datetime import timedelta


class Config:
    """Base Config"""
    # set listening port
    PORT = '8000'

    # set session config
    SECRET_KEY = 'secret_key'
    SESSION_COOKIE_NAME = 'SESSION_COOKIE_NAME'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)  # session will last for 5 minute

    API_MAX_RESULTS = 250


class ProdConfig(Config):
    """Production Config"""
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    """Development Config"""
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True


class TestConfig(Config):
    """Testing Config"""
    FLASK_ENV = 'testing'
    DEBUG = True
    TESTING = True


# config mapping
app_config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
}
