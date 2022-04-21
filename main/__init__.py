from sqlite3 import connect
import bcrypt
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "roomieapp",
    'host':'localhost',
    'port': 27017
}
# app.debug = True
bcrypt = Bcrypt(app)
loggin_manager =LoginManager(app)
db = MongoEngine(app)

from main import routes
