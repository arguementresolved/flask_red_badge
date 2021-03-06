
import requests
import json
from . import db, bcrypt
from marshmallow import Schema, fields


apiUrl = 'https://superheroapi.com/api/2137552436292179/'

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
    # battles = db.relationship('BattlesModel', backref='users', lazy=True)

    def __init__(self, data):
        self.Hero_names = data.get('Hero_names')
        self.Results = data.get('Results')
        self.created_at = datetime.datetime.utcnow()

    def __repr__(self):
        return f'<id {self.id}>'

    @staticmethod
    def get_name(value):
        return BattlesModel.query.filter_by(Hero_names=value).first()

    @staticmethod
    def get_fighter_id(fighter_id):

        g = requests.get(f'{apiUrl}{fighter_id}')
        json_data = json.loads(g.text)
        x = {
            'id': json_data['id'],
            'name': json_data['name'],
            'intelligence': json_data['powerstats']['intelligence'],
            'strength': json_data['powerstats']['strength'],
            'speed': json_data['powerstats']['speed'],
            'durability': json_data['powerstats']['durability'],
            'power': json_data['powerstats']['power'],
            'combat': json_data['powerstats']['combat']
        },

        return x

    @staticmethod
    def get_powerstats(fighter_id):

        g = requests.get(f'{apiUrl}{fighter_id}')
        json_data = json.loads(g.text)
        x = {
            'name': json_data['name'],
            'intelligence': json_data['powerstats']['intelligence'],
            'strength': json_data['powerstats']['strength'],
            'speed': json_data['powerstats']['speed'],
            'durability': json_data['powerstats']['durability'],
            'power': json_data['powerstats']['power'],
            'combat': json_data['powerstats']['combat']
        },

        return x


class BattlesSchema(Schema):
    id = fields.Int(dump_only=True)
    Hero_names = fields.Str(required=True)
    Results = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)
    battles = fields.DateTime(dump_only=True)



# import requests
# import json
# from . import db, bcrypt
# from marshmallow import Schema, fields
# import datetime


# apiUrl = 'https://superheroapi.com/api/2137552436292179/'

# # Example:
# # https://superheroapi.com/try-now.html

# # API source rights: Copyright 2017 © TwentyEight10


# class BattlesModel(db.Model):
#     __tablename__ = 'battles'

#     id = db.Column(db.Integer, primary_key=True)
#     owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     results = db.Column(db.String(128))
#     created_at = db.Column(db.DateTime)

#     def __init__(self, data):
#         self.owner_id = data.get('owner_id')
#         self.results = data.get('results')
#         self.created_at = datetime.utcnow()

#     def __repr__(self):
#         return f'<id {self.id}>'

#     @staticmethod
#     def get_one_user(id):
#         return BattlesModel.query.filter_by(id=id).first()

#     @staticmethod
#     def get_all_battles():
#         return BattlesModel.query.all()

#     @staticmethod
#     def get_users_battle(owner_id):
#         return BattlesModel.query.get(owner_id)

#     @staticmethod
#     def get_name(value):
#         return BattlesModel.query.filter_by(Hero_names=value).first()

#     @staticmethod
#     def get_fighter_id(fighter_id):

#         g = requests.get(f'{apiUrl}{fighter_id}')
#         json_data = json.loads(g.text)
#         x = {
#             'id': json_data['id'],
#             'name': json_data['name'],
#             'intelligence': json_data['powerstats']['intelligence'],
#             'strength': json_data['powerstats']['strength'],
#             'speed': json_data['powerstats']['speed'],
#             'durability': json_data['powerstats']['durability'],
#             'power': json_data['powerstats']['power'],
#             'combat': json_data['powerstats']['combat']
#         },

#         return x

#     @staticmethod
#     def get_powerstats(fighter_id):

#         g = requests.get(f'{apiUrl}{fighter_id}')
#         json_data = json.loads(g.text)
#         x = {
#             'name': json_data['name'],
#             'intelligence': json_data['powerstats']['intelligence'],
#             'strength': json_data['powerstats']['strength'],
#             'speed': json_data['powerstats']['speed'],
#             'durability': json_data['powerstats']['durability'],
#             'power': json_data['powerstats']['power'],
#             'combat': json_data['powerstats']['combat']
#         },

#         return x


# class BattlesSchema(Schema):
#     id = fields.Int(dump_only=True)
#     owner_id = fields.Int(dump_only=True)
#     results = fields.String(required=True)
#     created_at = fields.DateTime(dump_only=True)
