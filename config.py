import os
class Config:
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://june:1234@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS= False

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):

    pass
class DevConfig(Config):

    DEBUG=True

config_options={
    'development':DevConfig,
    'production':ProdConfig
    }
