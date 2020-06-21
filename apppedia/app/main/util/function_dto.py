from flask_restplus import Namespace, fields

class FunctionDto:
    api = Namespace('function', description='function related operations')
    function = api.model('function', {
        'public_id': fields.String(description='function public id'),
        'application_public_id': fields.String(required=True, description='function application public id'),
        'detail': fields.String(required=True, description='function detail'),
    })