# SETUP PROFILE ENDPOINTS BY THE END OF THE DAY
# from profile import ProfileModel
from flask import request, json, Response, Blueprint, g
from ..models.user import UserModel, UserSchema
from ..models.profile import ProfileModel, ProfileSchema
from ..shared.authentication import Auth

profile_api = Blueprint('profiles', __name__)
profile_schema = ProfileSchema()

# @user_api.route('/<int:user_id>', methods=['POST'])
# @Auth.auth_required
# def create_profile(user_id):
    
#     req_data = requests.get_json()
    
@profile_api.route('/', methods=['POST'])
def create():
    '''
    Create endpoint for user api
    '''

    req_data = request.get_json()
    data, error = profile_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    # check if user already exists in db
    profile_in_db = ProfileModel.get_user_by_id(data.get('id'))
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

