import uuid

from app.main import db
from app.main.model.favorites import Favorites
from app.main.model.application import Application

def favorites_list(user_email):
    return Favorites.query.filter_by(user_email=user_email).all()

def favorites_save(data):
    application = Application.query.filter_by(public_id=data['application_public_id']).first()
    favorites = Favorites.query.filter_by(user_email=data['user_email']).filter_by(application_public_id=data['application_public_id']).first()
    if not favorites:
        new_favorites = Favorites(
            public_id=str(uuid.uuid4()),
            user_email=data['user_email'],
            application_public_id=data['application_public_id'],
            application_name=application.name,
            application_category=application.category,
            application_rating_average=application.rating_average,
            application_image_logo=application.image_logo,
            application_price=application.price
        )
        save_changes(new_favorites)
        response_object = {
            'status': 'success',
            'message': 'Successfully saved.',
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'favorites already exists.',
        }
        return response_object, 409

def favorites_remove(public_id):
    favorites = Favorites.query.filter_by(public_id=public_id).first()
    remove_changes(favorites)
    response_object = {
        'status': 'success',
        'message': 'Successfully removed.',
    }
    return response_object, 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def remove_changes(data):
    db.session.delete(data)
    db.session.commit()