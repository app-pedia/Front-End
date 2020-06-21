from app.main import db
from app.main.model.developer import Developer

def developer_save(data):
    developer = Developer.query.filter_by(public_id=data['public_id']).first()
    if not developer:
        new_developer = Developer(
            public_id = data['public_id'],
            name = data['name'],
            country = data['country'],
            address = data['address'],
            web = data['web'],
            rating_total = data['rating_total'],
            rating_average = data['rating_average'],
            install_achieved = data['install_achieved']
        )
        save_changes(new_developer)
        response_object = {
            'status': 'success',
            'message': 'Successfully saved.',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'developer already exists.',
        }
        return response_object, 409

def developer_info(public_id):
    return Developer.query.filter_by(public_id=public_id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()