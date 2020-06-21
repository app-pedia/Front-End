from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.user_dto import UserDto
from ..service.user_service import user_logup, user_info, user_modify

api = UserDto.api
_user = UserDto.user

@api.route('/logup')
class UserLogUp(Resource):
    @api.expect(_user, validate=True)
    @api.response(201, 'user registered')
    @api.doc('user logup')
    def post(self):
        """ user logup """
        data = request.json
        return user_logup(data=data)

@api.route('/info/<email>')
@api.param('email', 'user email')
@api.response(404, 'user info unknown')
class ApplicationInfo(Resource):
    @token_required
    @api.doc('user info')
    @api.marshal_with(_user)
    def post(self, email):
        """ user info """
        user = user_info(email)
        return user

@api.route('/modify')
class UserLogUp(Resource):
    @token_required
    @api.expect(_user, validate=True)
    @api.response(201, 'user modified')
    @api.doc('user modify')
    def post(self):
        """ user modify """
        data = request.json
        return user_modify(data=data)