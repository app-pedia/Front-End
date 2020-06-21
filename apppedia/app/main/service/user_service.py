import uuid
import datetime

from app.main import db
from app.main.model.user import User

def user_logup(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            registered_on=datetime.datetime.utcnow(),
            public_id=str(uuid.uuid4()),
            username=data['username'],
            password=data['password'],
            device_name=data['device_name'],
            android_version=data['android_version']
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

def user_info(email):
    return User.query.filter_by(email=email).first()

def user_modify(data):
    user = User.query.filter_by(email=data['email']).first()
    if user:
        user.username = data['username']
        user.device_name = data['device_name']
        user.android_version = data['android_version']
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully modified.',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User has no information.',
        }
        return response_object, 409

def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def save_changes(data):
    db.session.add(data)
    db.session.commit()