from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models.db_models import User
from app_configured.configure import db

user_routes = Blueprint('user_routes', __name__)

def is_admin():
    current_user_email = get_jwt_identity()
    user = User.query.filter_by(email=current_user_email).first()
    return user and user.role == 'admin'

# Get all users (Admin only)
@user_routes.route('/', methods=['GET'])
@jwt_required()
def get_users():
    if not is_admin():
        return jsonify(message='Admin access required'), 403
    users = User.query.all()
    users_list = [{'id': user.id, 'email': user.email, 'username': user.username, 'role': user.role} for user in users]
    return jsonify(users=users_list), 200

# Get a single user's info (Admin or self)
@user_routes.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    current_user = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify(message='User not found'), 404

    if is_admin() or current_user == user.email:
        return jsonify(id=user.id, email=user.email, username=user.username, role=user.role), 200

    return jsonify(message='Unauthorized'), 403

# Update user info (Self or Admin)
@user_routes.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    current_user = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify(message='User not found'), 404
    if current_user != user.email and not is_admin():
        return jsonify(message='Unauthorized'), 403

    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if username:
        user.username = username
    if email:
        user.email = email
    if password:
        user.password = generate_password_hash(password)

    db.session.commit()
    return jsonify(message='User updated successfully'), 200

# Delete a user (Admin only)
@user_routes.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    if not is_admin():
        return jsonify(message='Admin access required'), 403

    user = User.query.get(user_id)
    if not user:
        return jsonify(message='User not found'), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify(message='User deleted successfully'), 200
