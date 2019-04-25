# SETUP PROFILE ENDPOINTS BY THE END OF THE DAY
# from profile import ProfileModel
from flask import request, json, Response, Blueprint, g
from ..models.user import UserModel, UserSchema
from ..models.profile import ProfileModel, ProfileSchema
from ..shared.authentication import Auth

profile_api = Blueprint('profiles', __name__)
profile_schema = ProfileSchema()


@profile_api.route('/', methods=["GET"])
@Auth.auth_required
def profile():
    req_data = request.get_json()
    data, error = profile_schema.load(req_data)
    user = ProfileModel(data)
    user.save()
    owner_id = ProfileModel.get_one_user(g.user.get('owner_id'))
    if not owner_id:
        return custom_response({'error': 'user not found'}, 404)

    ser_user = profile_schema.dump(owner_id).data
    return custom_response(ser_user, 200)


@profile_api.route('/<int:id>', methods=["GET"])
# @Auth.auth_required
def get_me(id):
    '''
    Get owners user information (me)
    '''
    pro_data = request.get_json()
    data = profile_schema.load(pro_data)
    user = ProfileModel.get_one_user(id)
    if not user:
        return custom_response({'error': "user not found"}, 404)
    pro_user = profile_schema.dump(user).data
    return custom_response(pro_user, 200)


def custom_response(res, status_code):
    '''
    Creates a custom json response
    for proper status messages
    '''

    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
