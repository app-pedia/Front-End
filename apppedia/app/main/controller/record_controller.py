from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.record_dto import RecordDto
from ..service.record_service import record_list, record_save, record_remove

api = RecordDto.api
_record = RecordDto.record

@api.route('/list/<user_email>')
@api.param('user_email', 'record user email')
@api.response(404, 'record list unknown')
class RecordList(Resource):
    @token_required
    @api.doc('record list')
    @api.marshal_with(_record)
    def post(self, user_email):
        """ record list """
        record = record_list(user_email)
        return record

@api.route('/save')
class RecordSave(Resource):
    @token_required
    @api.expect(_record, validate=True)
    @api.response(201, 'record saved.')
    @api.doc('record save')
    def post(self):
        """ record save """
        data = request.json
        return record_save(data=data)

@api.route('/remove/<public_id>')
@api.param('public_id', 'record public id')
class RecordRemove(Resource):
    @token_required
    @api.doc('record remove')
    @api.response(201, 'record removed.')
    @api.marshal_with(_record)
    def post(self, public_id):
        """ record remove """
        return record_remove(public_id)