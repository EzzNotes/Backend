from flask import Flask
from flask_login import LoginManager

#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

def create_App():
    app = Flask(__name__)
    app.config["SECURE_KEY"] = "lkjhgfdsa"

    #  -------------------------------- Database Setup (Not in use anymore) --------------------------------
    #app.config["SQLAlchemy_DATABASE_URL"] = "sqlite://db.sqlite3"
    #db.init_app(app)

    from .auth import Auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import Main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app