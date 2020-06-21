import uuid

from app.main import db
from app.main.model.function import Function

def function_save(data):
    new_function = Function(
        public_id=str(uuid.uuid4()),
        application_public_id=data['application_public_id'],
        detail=data['detail']
    )
    save_changes(new_function)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.',
    }
    return response_object, 200

def function_list(application_public_id):
    return Function.query.filter_by(application_public_id=application_public_id).all()

def save_changes(data):
    db.session.add(data)
    db.session.commit()