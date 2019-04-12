
import requests
import json
from . import db, bcrypt
from marshmallow import Schema, fields


apiUrl = 'https://superheroapi.com/api/2137552436292179/';

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
            'name': json_data['name'],
            'id': json_data['id'],
            'powerstats': json_data['powerstats']
        },

        return x

    @staticmethod
    def get_powerstats(fighter_id):
        
        g = requests.get(f'{apiUrl}{fighter_id}')
        json_data = json.loads(g.text)
        x = {
            'name': json_data['name'],
            'powerstats': json_data['powerstats']
        },

        return x

    # I'm going to write this mostly for me and my thought process
    # it might help you
    # the "get_fighter_id" needs to be able to send a input of numbers to the 
    # superhero api then return that hero's info
    # so you need to beable to take in a fighter_id and send a get request
    # then return that hero's ifnormation the function that calls this

    # def get_fighter_id(id):
    #     return BattlesModel.query.get()



class BattlesSchema(Schema):
    id = fields.Int(dump_only=True)
    Hero_names = fields.Str(required=True)
    Results = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)
    battles = fields.DateTime(dump_only=True)
