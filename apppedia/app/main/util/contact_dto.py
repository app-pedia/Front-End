from flask_restplus import Namespace, fields

class ContactListDto:
    api = Namespace('contact', description='contact related operations')
    contact = api.model('contact_list', {
        'public_id': fields.String(description='contact public id'),
        'user_email': fields.String(required=True, description='contact user email'),
        'title': fields.String(required=True, description='contact title'),
    })

class ContactInfoDto:
    api = Namespace('contact', description='contact related operations')
    contact = api.model('contact_info', {
        'public_id': fields.String(description='contact public id'),
        'user_email': fields.String(required=True, description='contact user email'),
        'title': fields.String(required=True, description='contact title'),
        'content': fields.String(required=True, description='contact content'),
    })