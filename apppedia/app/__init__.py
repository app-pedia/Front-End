from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.record_controller import api as record_ns
from .main.controller.application_controller import auto_api as application_auto_ns
from .main.controller.application_controller import srch_api as application_srch_ns
from .main.controller.application_controller import comp_api as application_comp_ns
from .main.controller.application_controller import info_api as application_info_ns
from .main.controller.application_controller import plus_api as application_plus_ns
from .main.controller.developer_controller import api as developer_ns
from .main.controller.function_controller import api as function_ns
from .main.controller.favorites_controller import save_api as favorites_save_ns
from .main.controller.favorites_controller import list_api as favorites_list_ns
from .main.controller.contact_controller import list_api as contact_list_ns
from .main.controller.contact_controller import info_api as contact_info_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='APPPEDIA : APPLICATION ENCYCLOPEDIA SERVICES',
          version='1.0',
          description='FRAMEWORK : FLASK\nLANGUAGE  : PYTHON\nAPI       : RESTPLUS\nCODE      : BOILER-PLATE\nTOKEN     : JSON WEB TOKEN'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(record_ns, path='/record')
api.add_namespace(application_auto_ns, path='/application')
api.add_namespace(application_srch_ns, path='/application')
api.add_namespace(application_comp_ns, path='/application')
api.add_namespace(application_info_ns, path='/application')
api.add_namespace(application_plus_ns, path='/application')
api.add_namespace(developer_ns, path='/developer')
api.add_namespace(function_ns, path='/function')
api.add_namespace(favorites_save_ns, path='/favorites')
api.add_namespace(favorites_list_ns, path='/favorites')
api.add_namespace(contact_list_ns, path='/contact')
api.add_namespace(contact_info_ns, path='/contact')
