from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from config import Config

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # Blueprint principal
    from app.routes import main
    app.register_blueprint(main)

    # Blueprint de gestión (CRUD)
    from app.gestion.routes import gestion_bp
    app.register_blueprint(gestion_bp)

    return app