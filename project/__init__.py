from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'appsforthepeople'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from .sdata import sdata as sdata_blueprint
    app.register_blueprint(sdata_blueprint.sdata)

    return app