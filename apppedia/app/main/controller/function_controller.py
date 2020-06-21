from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.function_dto import FunctionDto
from ..service.function_service import function_save, function_list

api = FunctionDto.api
_function = FunctionDto.function


@api.route('/save')
class FunctionSave(Resource):
    @api.expect(_function, validate=True)
    @api.response(201, 'function saved.')
    @api.doc('function save')
    def post(self):
        """ function save """
        data = request.json
        return function_save(data=data)

@api.route('/list/<application_public_id>')
@api.param('application_public_id', 'function application public id')
@api.response(404, 'function list unknown')
class RelatedList(Resource):
    @token_required
    @api.doc('function list')
    @api.marshal_with(_function)
    def post(self, application_public_id):
        """ function list """
        function = function_list(application_public_id)
        return function