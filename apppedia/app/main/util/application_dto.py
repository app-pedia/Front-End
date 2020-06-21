from flask_restplus import Namespace, fields

class ApplicationAutoDto:
    api = Namespace('application', description='application related operations')
    application_auto = api.model('application_auto', {
        'name': fields.String(description='application name'),
    })

class ApplicationSrchDto:
    api = Namespace('application', description='application related operations')
    application_srch = api.model('application_srch', {
        'word': fields.String(required=True, description='application search word'),
        'category': fields.String(description='application search categry'),
        'developer_name': fields.String(description='application search developer name'),
        'rating_upper_total': fields.String(description='application search total rating upper'),
        'rating_lower_total': fields.String(description='application search total rating lower'),
        'rating_upper_average': fields.String(description='application search average rating upper'),
        'rating_lower_average': fields.String(description='application search average rating lower'),
        'install_upper': fields.String(description='application search install upper'),
        'install_lower': fields.String(description='application search install lower'),
        'price_upper': fields.String(description='application search price upper'),
        'price_lower': fields.String(description='application search price lower'),
        'version_needs': fields.String(description='application search needs version upper'),
        'function_five': fields.String(description='application search function five'),
        'function_four': fields.String(description='application search function four'),
        'function_three': fields.String(description='application search function three'),
        'function_two': fields.String(description='application search function two'),
        'function_one': fields.String(description='application search function one'),
    })
    application_rslt = api.model('application_rslt', {
        'public_id': fields.String(required=True, description='application public id'),
        'name': fields.String(description='application name'),
        'category': fields.String(description='application category'),
        'rating_average': fields.String(description='application average rating'),
        'image_logo': fields.String(description='application image logo'),
        'price': fields.String(description='application price'),
    })

class ApplicationCompDto:
    api = Namespace('application', description='application related operations')
    application_comp = api.model('application_comp', {
        'public_id': fields.String(required=True, description='application compare public id'),
        'function_five': fields.String(description='application compare function five'),
        'function_four': fields.String(description='application compare function four'),
        'function_three': fields.String(description='application compare function three'),
        'function_two': fields.String(description='application compare function two'),
        'function_one': fields.String(description='application compare function one'),
    })
    application_rult = api.model('application_rult', {
        'public_id': fields.String(required=True, description='application public id'),
        'name': fields.String(description='application name'),
        'category': fields.String(description='application category'),
        'image_logo': fields.String(description='application image logo'),
        'score_all': fields.String(description='application score all'),
        'score_rating_average': fields.String(description='application score average rating'),
        'score_rating_total': fields.String(description='application score total rating'),
        'score_install': fields.String(description='application score total rating'),
        'score_function_five': fields.String(description='application score function five'),
        'score_function_four': fields.String(description='application score function four'),
        'score_function_three': fields.String(description='application score function three'),
        'score_function_two': fields.String(description='application score function two'),
        'score_function_one': fields.String(description='application score function one'),
    })

class ApplicationInfoDto:
    api = Namespace('application', description='application related operations')
    application_info = api.model('application_info', {
        'public_id': fields.String(required=True, description='application public id'),
        'name': fields.String(description='application name'),
        'category': fields.String(description='application category'),
        'developer_name': fields.String(description='application developer name'),
        'developer_public_id': fields.String(description='application developer public id'),
        'rating_total': fields.String(description='application total rating'),
        'rating_average': fields.String(description='application average rating'),
        'rating_five': fields.String(description='application five star rating'),
        'rating_four': fields.String(description='application four star rating'),
        'rating_three': fields.String(description='application three star rating'),
        'rating_two': fields.String(description='application two star rating'),
        'rating_one': fields.String(description='application one star rating'),
        'install': fields.String(description='application install'),
        'install_link': fields.String(description='application link install'),
        'image_logo': fields.String(description='application image logo'),
        'price': fields.String(description='application price'),
        'update_date': fields.String(description='application update date'),
        'size': fields.String(description='application size'),
        'version_current': fields.String(description='application current version'),
        'version_needs': fields.String(description='application needs version'),
        'contents_grade': fields.String(description='application contents grade'),
        'interaction': fields.String(description='application interaction'),
        'in_app_products': fields.String(description='application in app products'),
        'related_name': fields.String(description='application related name'),
        'related_link': fields.String(description='application related link'),
    })

class ApplicationPlusDto:
    api = Namespace('application', description='application related operations')
    application_plus = api.model('application_plus', {
        'category': fields.String(description='application category'),
        'related_name': fields.String(description='application related name'),
        'related_link': fields.String(description='application related link'),
    })