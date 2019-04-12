from flask import json, request, Response, Blueprint, g
from ..shared.authentication import Auth
from ..models.battles import BattlesModel, BattlesSchema
import requests

battles_api = Blueprint('battles', __name__)
battles_schema = BattlesSchema()

@battles_api.route('/recent', methods=['POST'])

def get_fighter():
    '''
    Get info from ID, off of the API
    '''
   
    req_data = request.get_json()
    fighter_id = req_data['fighter_id']
   
    fighter = BattlesModel.get_fighter_id(fighter_id)
    if not fighter:
        return custom_response({'error': 'Figher not found!'}, 404)

    ser_battles = battles_schema.dump(battles).data
    return custom_response(ser_battles, 200)


@battles_api.route('/new', methods=['POST'])
@Auth.auth_required
def create():
   
    '''
    Create endpoint for battles api
    '''

    req_data = request.get_json()
    data, error = battles_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    # check if user already exists in db
    battles_in_db = BattlesModel.get_name(data.get('Hero_names'))
    if battles_in_db:
        message = {'error': 'User already exists, please supply another email address'}
        return custom_response(message, 400)

    user = BattlesModel(data)
    user.save()

    ser_data = user_schema.dump(user).data

    token = Auth.generate_token(ser_data.get('id'))

    return custom_response({'token': token}, 201)

@battles_api.route('/calc', methods=["POST"])
def battleFunc():
    '''
    INPUT HERO NUMBER
    '''

    req_data = request.get_json()
    req_data["k"] = k
    req_data["l"] = l

    # JSON REQUEST AND PROCCESSING OF API
    r = request.get(f'https://superheroapi.com/api/2137552436292179/{}/powerstats'.format(k))
    json_data_1 = json.loads(r.text)

    q = request.get(f'https://superheroapi.com/api/2137552436292179/{}/powerstats'.format(l))
    json_data_2 = json.loads(q.text)


    '''
    STARTING COUNTERS
    '''
    x = 0   # [letter]1
    y = 0   # [letter]2

    '''
    HERO 1

    This takes in the stats of the 1st inputted hero from the API, checks for nulls,
    and takes the name of the first hero.
    '''
    for i in json_data_1:
        if i == 'name':
            z1 = json_data_1[i]
        if i == 'intelligence':
            if (json_data_1[i]) == 'null':
                a1 = 0
            else:
                a1 = int(json_data_1[i])
        if i == 'strength':
            if (json_data_1[i]) == 'null':
                b1 = 0
            else:
                b1 = int(json_data_1[i])
        if i == 'speed':
            if (json_data_1[i]) == 'null':
                c1 = 0
            else:
                c1 = int(json_data_1[i])
        if i == 'durability':
            if (json_data_1[i]) == 'null':
                d1 = 0
            else:
                d1 = int(json_data_1[i])
        if i == 'power':
            if (json_data_1[i]) == 'null':
                e1 = 0
            else:
                e1 = int(json_data_1[i])
        if i == 'combat':
            if (json_data_1[i]) == 'null':
                f1 = 0
            else:
                f1 = int(json_data_1[i])
    g1 = a1 + b1 + c1 + d1 + e1 + f1

    '''
    HERO 2

    This takes in the stats of the 2nd inputted hero from the API, checks for nulls,
    and takes the name of the second hero.
    '''
    for i in json_data_2:
        if i == 'name':
            z2 = json_data_2[i]
        if i == 'intelligence':
            if (json_data_2[i]) == 'null':
                a2 = 0
            else:
                a2 = int(json_data_2[i])
        if i == 'strength':
            if (json_data_2[i]) == 'null':
                b2 = 0
            else:
                b2 = int(json_data_2[i])
        if i == 'speed':
            if (json_data_2[i]) == 'null':
                c2 = 0
            else:
                c2 = int(json_data_2[i])
        if i == 'durability':
            if (json_data_2[i]) == 'null':
                d2 = 0
            else:
                d2 = int(json_data_2[i])
        if i == 'power':
            if (json_data_2[i]) == 'null':
                e2 = 0
            else:
                e2 = int(json_data_2[i])
        if i == 'combat':
            if (json_data_2[i]) == 'null':
                f2 = 0
            else:
                f2 = int(json_data_2[i])
    g2 = a2 + b2 + c2 + d2 + e2 + f2

    # ADDING TO COUNTERS, USING THE "WIN POINTS"
    # EXAMPLE: a1, b2, d1, etc..


    # INTELEGENCE
    '''
    Compares which hero has the higher stat in each area and awards points.
    '''
    if a1 > a2:
        x += 1
    elif a1 < a2:
        y += 1
    elif a1 == a2:
        x += 1
        y += 1

    # STRENGTH
    if b1 > b2:
        x += 1
    elif b1 < b2:
        y += 1
    elif b1 == b2:
        x += 1
        y += 1

    # SPEED
    if c1 > c2:
        x += 1
    elif c1 < c2:
        y += 1
    elif c1 == c2:
        x += 1
        y += 1

    # DURABILITY
    if d1 > d2:
        x += 1
    elif d1 < d2:
        y += 1
    elif d1 == d2:
        x += 1
        y += 1

    # POWER
    if e1 > e2:
        x += 1
    elif e1 < e2:
        y += 1
    elif e1 == a2:
        x += 1
        y += 1

    # COMBAT
    if f1 > f2:
        x += 1
    elif f1 < f2:
        y += 1
    elif f1 == f2:
        x += 1
        y += 1

    # OVERALL STATS NUMBER
    '''
    Calculates the stats from above and determines which hero is the winner.
    Also, it implements the TIEBREAKER Stat (g1 and g2), if needed.
    '''
    if x > y:
        print(f'{z1} would win!')
    elif x < y:
        print(f'{z2} would win!')
    elif x == y:
        if g1 > g2:
            print(f'{z1} would win!')
        elif g1 < g2:
            print(f'{z2} would win!')
        elif g1 == g2:
            print(f'{z1} vs. {z2} would result in a stalmate!')


def custom_response(res, status_code):

    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
