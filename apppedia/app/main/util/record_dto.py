from flask_restplus import Namespace, fields

class RecordDto:
    api = Namespace('record', description='record related operations')
    record = api.model('record', {
        'public_id': fields.String(description='record public id'),
        'user_email': fields.String(required=True, description='record user email'),
        'content': fields.String(required=True, description='record content'),
    })