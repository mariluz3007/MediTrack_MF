"""Rutas y formularios para la gestión de medicamentos."""
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from config import Config

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from app.routes import main
    from app.gestion.routes import gestion_bp

    app.register_blueprint(main)
    app.register_blueprint(gestion_bp)

    return app
