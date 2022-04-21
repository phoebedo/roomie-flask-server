from crypt import methods
from flask import request, jsonify
from main import app, db
from main.models import User
import logging

logging.basicConfig(level=logging.DEBUG)

@app.route("/")
@app.route("/home")
def home_page():
    return "HOMEPAGE"

@app.route('/register', methods=['GET','POST'])
def register_user():
    if methods == "POST":
        app.logger.info(request)
        data = request.form
        app.logger.info(f"Data from post request:{data}")

        new_user = User(
            username = request.form.get('username'),
            email_address = request.form.get('email_address'),
            password_hash = request.form.get('password')
        )
        new_user.save(force_insert=True)
        
    return "register page"
