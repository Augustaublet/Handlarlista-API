from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path

from flask_restful import Api

db = SQLAlchemy()
DB_NAME = "databas1.db"

from .routes import GetShoppingLists

def create_app():
    app = Flask(__name__)
    #app.config["SECRET_KEY"] = "August"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    CORS(app)
    api = Api(app)

    create_datebase(app)

    api.add_resource(GetShoppingLists, "/")
    return app
def create_datebase(app):
    if not path.exists("handlarwebapp/"+DB_NAME):
        db.create_all(app=app)


