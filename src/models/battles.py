
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
    # battles = db.relationship('BattlesModel', backref='users', lazy=True)

    def __init__(self, data):
        self.Hero_names = data.get('Hero_names')
        self.Results = data.get('Results')
        self.created_at = datetime.datetime.utcnow()

    def __repr__(self):
        return f'<id {self.id}>'


class BattlesSchema(Schema):
    id = fields.Int(dump_only=True)
    Hero_names = fields.Str(required=True)
    Results = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)
    battles = fields.DateTime(dump_only=True)
