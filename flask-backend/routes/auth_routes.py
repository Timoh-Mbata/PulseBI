from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models.db_models import User
from app_configured.configure import db

authentification = Blueprint('authentication', __name__,)

# Register a new user
@authentification.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not email or not password or not username:
        return jsonify(message='User name , Email and password are required'), 400
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify(message='User already exists'), 409
    hashed_password = generate_password_hash(password)
    new_user = User(username = username ,email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='User registered successfully'), 201

# Login and generate token
@authentification.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify(message='Email and password are required'), 400

    user = User.query.filter_by(email=email).first()  
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.email) 
        return jsonify(access_token=access_token), 200
    return jsonify(message='Invalid credentials'), 401

# Protected route to get current user
@authentification.route('/me', methods=['GET'])
@jwt_required()
def me():
    current_user = get_jwt_identity()  #
    return jsonify(email=current_user), 200

# Logout route (optional token blacklist logic can be added)
@authentification.route('/logout', methods=['POST'])
def logout():
    return jsonify(message='Logged out successfully (JWT not revoked)'), 200
