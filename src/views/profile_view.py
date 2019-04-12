# SETUP PROFILE ENDPOINTS BY THE END OF THE DAY
# from profile import ProfileModel
from flask import request, json, Response, Blueprint, g
from ..models.user import UserModel, UserSchema
from ..models.profile import ProfileModel, ProfileSchema
from ..shared.authentication import Auth

profile_api = Blueprint('profiles', __name__)
profile_schema = ProfileSchema()

@profile_api.route('/<int:owner_id>', methods=['GET'])
# read and update
# deletes with user


def get_user(owner_id):
    '''
    Get a single user
    '''
    user = ProfileModel.get_one_user(owner_id)
    if not user:
        return custom_response({'error': 'user not found'}, 404)

    ser_user = profile_schema.dump(user).data
    return custom_response(ser_user, 200)
    
@profile_api.route('/', methods=['POST'])
def create():
    '''
    Create endpoint for profile api
    '''

    req_data = request.get_json()
    data, error = profile_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    # check if user already exists in db
    profile_in_db = ProfileModel.get_user_by_username(data.get('username'))
    if profile_in_db:
        message = {'error': 'Profile already exists, please supply another email address'}
        return custom_response(message, 400)
    
    user = ProfileModel(data)
    user.save()

    pro_data = profile_schema.dump(user).data

    token = Auth.generate_token(pro_data['id'])

    return custom_response({'token': token}, 201)

@profile_api.route('/me', methods=["GET"])
@Auth.auth_required
def get_me():
    '''
    Get owners user information (me)
    '''

    user = ProfileModel.get_one_user(g.user.get('id'))
    pro_user = profile_schema.dump(profile).data
    return custom_response(pro_user, 200)

