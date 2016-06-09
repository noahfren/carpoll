from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.mail import Mail
from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .signup import signup as signup_blueprint
    app.register_blueprint(signup_blueprint, url_prefix='/signup')

    return app
