from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.contact_dto import ContactListDto, ContactInfoDto
from ..service.contact_service import contact_list, contact_info, contact_save

list_api = ContactListDto.api
info_api = ContactInfoDto.api

_contact_list = ContactListDto.contact
_contact_info = ContactInfoDto.contact

@list_api.route('/list/<user_email>')
@list_api.param('user_email', 'contact user email')
@list_api.response(404, 'contact list unknown')
class ContactList(Resource):
    @token_required
    @list_api.doc('contact list')
    @list_api.marshal_with(_contact_list)
    def post(self, user_email):
        """ contact list """
        contact = contact_list(user_email)
        return contact

@info_api.route('/info/<public_id>')
@info_api.param('public_id', 'contact public id')
@info_api.response(404, 'contact info unknown')
class ContactInfo(Resource):
    @token_required
    @info_api.doc('contact info')
    @info_api.marshal_with(_contact_info)
    def post(self, public_id):
        """ contact info """
        contact = contact_info(public_id)
        return contact

@info_api.route('/save')
class ContactSave(Resource):
    @token_required
    @info_api.expect(_contact_info, validate=True)
    @info_api.response(201, 'contact saved.')
    @info_api.doc('contact save')
    def post(self):
        """ contact save """
        data = request.json
        return contact_save(data=data)