#Donde se configará la base de datos (usando SQLAlchemy), el modo de depuración, y 
# otras variables de configuración necesarias.
import os

BASE_DIR = os.path.abspath(os.path.dirname(__init__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "development-only-change-me")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        BASE_DIR = os.path.abspath(os.path.dirname(file))
    )


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"
