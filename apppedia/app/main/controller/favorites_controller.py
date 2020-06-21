from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.favorites_dto import FavoritesSaveDto, FavoritesListDto
from ..service.favorites_service import favorites_list, favorites_save, favorites_remove

save_api = FavoritesSaveDto.api
list_api = FavoritesListDto.api

_favorites_save = FavoritesSaveDto.favorites
_favorites_list = FavoritesListDto.favorites

@list_api.route('/list/<user_email>')
@list_api.param('user_email', 'favorites user email')
@list_api.response(404, 'favorites list unknown')
class FavoritesList(Resource):
    @token_required
    @list_api.doc('favorites list')
    @list_api.marshal_with(_favorites_list)
    def post(self, user_email):
        """ favorites list """
        favorites = favorites_list(user_email)
        return favorites

@save_api.route('/save')
class FavoritesSave(Resource):
    @token_required
    @save_api.expect(_favorites_save, validate=True)
    @save_api.response(201, 'favorites saved.')
    @save_api.doc('favorites save')
    def post(self):
        """ favorites save """
        data = request.json
        return favorites_save(data=data)

@save_api.route('/remove/<public_id>')
@save_api.param('public_id', 'favorites public id')
class FavoritesRemove(Resource):
    @token_required
    @save_api.doc('favorites remove')
    @save_api.response(201, 'favorites removed.')
    @save_api.marshal_with(_favorites_save)
    def post(self, public_id):
        """ favorites remove """
        return favorites_remove(public_id)