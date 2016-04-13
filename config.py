import os

base = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
