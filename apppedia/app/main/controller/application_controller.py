from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.application_dto import ApplicationAutoDto, ApplicationSrchDto, ApplicationCompDto, ApplicationInfoDto, ApplicationPlusDto
from ..service.application_service import application_save, application_auto, application_srch, application_comp, application_info, application_plus

auto_api = ApplicationAutoDto.api
srch_api = ApplicationSrchDto.api
comp_api = ApplicationCompDto.api
info_api = ApplicationInfoDto.api
plus_api = ApplicationPlusDto.api

_application_auto = ApplicationAutoDto.application_auto
_application_srch = ApplicationSrchDto.application_srch
_application_rslt = ApplicationSrchDto.application_rslt
_application_comp = ApplicationCompDto.application_comp
_application_rult = ApplicationCompDto.application_rult
_application_info = ApplicationInfoDto.application_info
_application_plus = ApplicationPlusDto.application_plus

@info_api.route('/save')
class ApplicationSave(Resource):
    @info_api.expect(_application_info, validate=True)
    @info_api.response(201, 'application saved.')
    @info_api.doc('application save')
    def post(self):
        """ application save """
        data = request.json
        return application_save(data=data)

@auto_api.route('/auto')
@auto_api.response(404, 'application name unknown')
class ApplicationAuto(Resource):
    @token_required
    @auto_api.doc('application name')
    @auto_api.marshal_with(_application_auto)
    def post(self):
        """ application name """
        application = application_auto()
        return application

@srch_api.route('/srch')
class ApplicationSrch(Resource):
    token_required
    @srch_api.expect(_application_srch, validate=True)
    @srch_api.response(201, 'application srch.')
    @srch_api.marshal_with(_application_rslt)
    @srch_api.doc('application srch')
    def post(self):
        """ application srch """
        data = request.json
        return application_srch(data=data)

@comp_api.route('/comp')
class ApplicationSrch(Resource):
    token_required
    @comp_api.expect(_application_comp, validate=True)
    @comp_api.response(201, 'application comp.')
    @comp_api.marshal_with(_application_rult)
    @comp_api.doc('application comp')
    def post(self):
        """ application comp """
        data = request.json
        return application_comp(data=data)

@info_api.route('/info/<public_id>')
@info_api.param('public_id', 'application public id')
@info_api.response(404, 'application info unknown')
class ApplicationInfo(Resource):
    @token_required
    @info_api.doc('application info')
    @info_api.marshal_with(_application_info)
    def post(self, public_id):
        """ application info """
        application = application_info(public_id)
        return application

@plus_api.route('/plus/<category>')
@plus_api.param('category', 'application category')
@plus_api.response(404, 'application plus unknown')
class ApplicationPlus(Resource):
    token_required
    @plus_api.doc('application plus')
    @plus_api.marshal_with(_application_plus)
    def post(self, category):
        """ application plus """
        application = application_plus(category)
        return application