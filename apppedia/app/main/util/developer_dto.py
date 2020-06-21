from flask_restplus import Namespace, fields

class DeveloperDto:
    api = Namespace('developer', description='developer related operations')
    developer = api.model('developer', {
        'public_id': fields.String(required=True, description='developer public id'),
        'name': fields.String(description='developer name'),
        'country': fields.String(description='developer country'),
        'address': fields.String(description='developer address'),
        'web': fields.String(description='developer web'),
        'rating_total': fields.String(description='developer total rating'),
        'rating_average': fields.String(description='developer average rating'),
        'install_achieved': fields.String(description='developer achieved install'),
    })