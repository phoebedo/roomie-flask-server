import os
import bcrypt

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from config import mongoEngineConfig
from api.routes.userRoutes import userRoutes
from api.database.db import init_database

app = Flask(__name__)

app.config.from_pyfile('config.py')
app.config['MONGODB_SETTINGS'] = mongoEngineConfig

CORS(app)
bcrypt = Bcrypt(app)
loggin = LoginManager(app)
init_database(app)

app.register_blueprint(userRoutes, url_prefix='/api/v1')
if __name__ == "__main__":
    app.run()
