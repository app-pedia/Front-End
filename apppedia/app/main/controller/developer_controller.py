from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.developer_dto import DeveloperDto
from ..service.developer_service import developer_save, developer_info

api = DeveloperDto.api
_developer = DeveloperDto.developer


@api.route('/save')
class DeveloperSave(Resource):
    @api.expect(_developer, validate=True)
    @api.response(201, 'developer saved.')
    @api.doc('developer save')
    def post(self):
        """ developer save """
        data = request.json
        return developer_save(data=data)

@api.route('/info/<public_id>')
@api.param('public_id', 'developer public id')
@api.response(404, 'developer info unknown')
class ApplicationInfo(Resource):
    @token_required
    @api.doc('developer info')
    @api.marshal_with(_developer)
    def post(self, public_id):
        """ developer info """
        developer = developer_info(public_id)
        return developer