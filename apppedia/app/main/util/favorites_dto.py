from flask_restplus import Namespace, fields

class FavoritesSaveDto:
    api = Namespace('favorites', description='favorites related operations')
    favorites = api.model('favorites_save', {
        'user_email': fields.String(required=True, description='favorites user email'),
        'application_public_id': fields.String(required=True, description='favorites application public id'),
    })

class FavoritesListDto:
    api = Namespace('favorites', description='application related operations')
    favorites = api.model('favorites_list', {
        'public_id': fields.String(description='favorites public id'),
        'application_public_id': fields.String(required=True, description='favorites application public id'),
        'application_name': fields.String(description='favorites application name'),
        'application_category': fields.String(description='favorites application category'),
        'application_rating_average': fields.String(description='favorites application average rating'),
        'application_image_logo': fields.String(description='favorites application image logo'),
        'application_price': fields.String(description='favorites application price'),
    })