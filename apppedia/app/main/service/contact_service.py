import uuid

from app.main import db
from app.main.model.contact import Contact

def contact_list(user_email):
    return Contact.query.filter_by(user_email=user_email).all()

def contact_info(public_id):
    return Contact.query.filter_by(public_id=public_id).first()

def contact_save(data):
    new_contact = Contact(
        public_id=str(uuid.uuid4()),
        user_email=data['user_email'],
        title=data['title'],
        content=data['content']
    )
    save_changes(new_contact)
    response_object = {
        'status': 'success',
        'message': 'Successfully saved.',
    }
    return response_object, 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()