import uuid
import datetime

from app.main import db
from app.main.model.record import Record

def record_list(user_email):
    record = Record.query.filter_by(user_email=user_email).all()
    record.reverse()
    return record

def record_save(data):
    new_record = Record(
        public_id=str(uuid.uuid4()),
        registered_on=datetime.datetime.utcnow(),
        user_email=data['user_email'],
        content=data['content']
    )
    save_changes(new_record)
    response_object = {
        'status': 'success',
        'message': 'successfully saved.',
    }
    return response_object, 200

def record_remove(public_id):
    record = Record.query.filter_by(public_id=public_id).first()
    remove_changes(record)
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