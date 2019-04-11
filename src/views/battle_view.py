from flask import request, json, Response, Blueprint, g
from ..shared.authentication import Auth
from ..models.battles import BattlesModel

battles_api = Blueprint('battles', __name__)
# battles_schema = BattlesSchema()





@battles_api.route('/<int:fighter_id>', methods=['GET'])
@Auth.auth_required
def get_fighter(fighter_id):
    '''
    Get info from ID, off of the API
    '''
    fighter = BattlesModel.get_one_user(fighter_id)
    if not figher:
        return custom_response({'error': 'Figher not found!'}, 404)

    ser_battles = battles_schema.dump(battles).data
    return custom_response(ser_battles, 200)


# @battles_api.route('/', methods=['POST'])
# def create():
#     '''
#     Create endpoint for battles api
#     '''

#     req_data = request.get_json()
#     data, error = battles_schema.load(req_data)

#     if error:
#         return custom_response(error, 400)

#     # check if user already exists in db
#     battles_in_db = BattlesModel.get_user_by_email(data.get('email'))
#     if battles_in_db:
#         message = {'error': 'User already exists, please supply another email address'}
#         return custom_response(message, 400)

#     user = UserModel(data)
#     user.save()

#     ser_data = user_schema.dump(user).data

#     token = Auth.generate_token(ser_data.get('id'))

#     return custom_response({'token': token}, 201)
