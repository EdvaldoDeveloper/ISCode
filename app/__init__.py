from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__, template_folder="views", static_folder="public")
    app.config["SECRET_KEY"] = 'sec tstevv'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/teste"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)
    bootstrap.init_app(app)

    from app import routes
    routes.init_app(app)

    return app
