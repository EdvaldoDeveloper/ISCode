from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder="views", static_folder="public")
    app.config["SECRET_KEY"] = 'sec tstevv'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/teste"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)

    from app import routes
    routes.init_app(app)

    return app
