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

# Login route to authenticate user and return JWT token
@authentification.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify(message='Email and password are required'), 400

    # Check if user exists
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        # Get user role from the database
        role = user.role  # assuming there's a column 'role' in your User model

        # Create access token with email as identity (you could also include role here)
        access_token = create_access_token(identity=user.email)

        # Determine dashboard route based on role
        if role == 'user':
            dashboard_route = '/user-dashboard'
        elif role == 'admin':
            dashboard_route = '/admin-dashboard'
        else:
            dashboard_route = '/user-dashboard'  # fallback

        return jsonify(
            access_token=access_token,
            role=role,
            dashboard=dashboard_route,  # Send this dynamically to frontend
            username=user.email  # Optionally, send username or other relevant info
        ), 200

    return jsonify(message='Invalid credentials'), 401


# Function to get user by email
def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return user
    return None

# Protected route to get the current user
@authentification.route('/me', methods=['GET'])
@jwt_required()  # Ensures that the user must be authenticated
def me():
    current_user = get_jwt_identity()  # Get the email from the JWT token
    user = get_user_by_email(current_user)  # Fetch the user from the database

    if user is None:
        return jsonify(message="User not found"), 404

    return jsonify(email=current_user, username=user.username), 200

# Logout route (optional token blacklist logic can be added)
@authentification.route('/logout', methods=['POST'])
def logout():
    return jsonify(message='Logged out successfully (JWT not revoked)'), 200
