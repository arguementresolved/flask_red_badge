
import requests
import json
from . import db, bcrypt
from marshmallow import Schema, fields


# Example:
# https://superheroapi.com/try-now.html

# API source rights: Copyright 2017 © TwentyEight10

class BattlesModel(db.Model):
    __tablename__ = 'battles'

    id = db.Column(db.Integer, primary_key=True)
    Hero_names = db.Column(db.String(128), nullable=False)
    Results = db.Column(db.String(128), unique=True, nullable=False)
    created_at = db.Column(db.DateTime)
    # navigational property
    battles = db.relationship('BattlesModel', backref='users', lazy=True)

    def __init__(self, data):
        self.Hero_names = data.get('Hero_names')
        self.Results = data.get('Results')
        self.created_at = datetime.datetime.utcnow()

    def __repr__(self):
        return f'<id {self.id}>'

    def battleFunc():
        '''
        INPUT HERO NUMBER
        '''
        k = input("Enter a number 1 - 731\n> ")
        l = input("Enter a number 1 - 731\n> ")
        print("Simulating Battle...")
        # JSON REQUEST AND PROCCESSING OF API
        r = requests.get(f'https://superheroapi.com/api/2137552436292179/{k}/powerstats')
        json_data_1 = json.loads(r.text)

        q = requests.get(f'https://superheroapi.com/api/2137552436292179/{l}/powerstats')
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

class BattlesSchema(Schema):
    id = fields.Int(dump_only=True)
    Hero_names = fields.Str(required=True)
    Results = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)
    battles = fields.DateTime(dump_only=True)
