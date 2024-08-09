from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .routes import main_blueprint  # Importa o Blueprint
        app.register_blueprint(main_blueprint)  # Registra o Blueprint
        db.create_all()

    return app