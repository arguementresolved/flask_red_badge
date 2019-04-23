from flask import json, request, Response, Blueprint, g
from ..shared.authentication import Auth
from ..models.battles import BattlesModel, BattlesSchema
from ..models.user import UserModel
import requests

battles_api = Blueprint('battles', __name__)
battles_schema = BattlesSchema()


@battles_api.route('/search', methods=['POST'])
def get_fighter():
    '''
    Get info from ID, off of the API
    '''
    req_data = request.get_json()
    fighter_id = req_data['fighter_id']

    fighter = BattlesModel.get_fighter_id(fighter_id)
    if not fighter:
        return custom_response({'error': 'Fighter not found!'}, 404)

    return custom_response(fighter, 200)


@battles_api.route('/calc', methods=["POST"])
@Auth.auth_required
def battleFunc():
    '''
    Input hero id - do this through "k" for fighter #1 and "l" for fighter 2
    '''

    req_data = request.get_json()
    k = req_data["fighter1"]
    l = req_data["fighter2"]

    # JSON REQUEST AND PROCCESSING OF API
    json_data_1 = BattlesModel.get_powerstats(k)
    json_data_2 = BattlesModel.get_powerstats(l)

    z1 = json_data_1[0]['name']
    a1 = json_data_1[0]['intelligence']
    b1 = json_data_1[0]['strength']
    c1 = json_data_1[0]['speed']
    d1 = json_data_1[0]['durability']
    e1 = json_data_1[0]['power']
    f1 = json_data_1[0]['combat']

    z2 = json_data_2[0]['name']
    a2 = json_data_2[0]['intelligence']
    b2 = json_data_2[0]['strength']
    c2 = json_data_2[0]['speed']
    d2 = json_data_2[0]['durability']
    e2 = json_data_2[0]['power']
    f2 = json_data_2[0]['combat']

    '''
    STARTING COUNTERS
    '''
    x = 0   # [letter]1
    y = 0   # [letter]2

    '''
    HERO 1
    This takes in the stats of the 1st inputted hero from
    the API, checks for nulls,
    and takes the name of the first hero.
    '''

    for i in json_data_1:
        if i == 'name':
            z1 = i
        if i == 'intelligence':
            if i == 'null':
                a1 = 0
            else:
                a1 = i
                print(i,'================================================')
        if i == 'strength':
            if i == 'null':
                b1 = 0
            else:
                b1 = i
        if i == 'speed':
            if i == 'null':
                c1 = 0
            else:
                c1 = i
        if i == 'durability':
            if i == 'null':
                d1 = 0
            else:
                d1 = i
        if i == 'power':
            if i == 'null':
                e1 = 0
            else:
                e1 = i
        if i == 'combat':
            if i == 'null':
                f1 = 0
            else:
                f1 = i
    g1 = a1 + b1 + c1 + d1 + e1 + f1

    '''
    HERO 2
    This takes in the stats of the 2nd inputted hero
    from the API, checks for nulls,
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
        winner = f'{z1} vs. {z2}:\n {z1} would win!'
    elif x < y:
        winner = f'{z1} vs. {z2}:\n {z2} would win!'
    elif x == y:
        if g1 > g2:
            winner = f'{z1} vs. {z2}:\n {z1} would win!'
        elif g1 < g2:
            winner = f'{z1} vs. {z2}:\n {z2} would win!'
        elif g1 == g2:
            winner = f'{z1} vs. {z2} would result in a stalmate!'

    # owner_id = BattlesModel.get_one_user(g.battles.get('owner_id'))
    # print(owner_id, '===================================')
    # results = {
    #     'owner_id': owner_id,
    #     'results': winner
    # }

    # data = battles_schema.load(results)
    # battle = BattlesModel(data)
    # battle.save()
    return custom_response(winner, 200)


# @battles_api.route('/', methods=['GET'])
# def get_all():
#     Results = BattlesModel.get_all_battles()
#     data = BattlesSchema.dump(Results, many=True).data
#     return custom_response(data, 200)


# @battles_api.route('/userFights', methods=["GET"])
# @Auth.auth_required
# def get_one():

#     req_data = request.get_json()
#     data, error = battles_schema.load(req_data)

#     Results = BattlesModel.get_users_battle(req_data)

#     if not Results:
#         return custom_response({'error': 'post not found'}, 404)

#     data = BattlesSchema.dump(Results).data

#     return custom_response(data, 200)


def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
