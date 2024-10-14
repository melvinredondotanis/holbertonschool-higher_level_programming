#!/usr/bin/env python
"""Task 5: Basic Security"""

from flask import Flask
from flask import jsonify
from flask import request

from flask_httpauth import HTTPBasicAuth

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    check = check_password_hash(users[username]['password'], password)
    if username in users and check:
        return username


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Basic protected route"""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return 401

    if check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200

    return 401


if __name__ == "__main__":
    app.run(debug=True)
