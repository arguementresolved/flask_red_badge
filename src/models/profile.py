from . import db, bcrypt
from datetime import datetime

from marshmallow import fields, Schema


class ProfileModel(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime)
    username = db.Column(db.String(250), unique=True)
    ProfilePic = db.Column(db.String(250), nullable=True)
    bio = db.Column(db.String(250), nullable=True)

    def __init__(self, data):
        self.owner_id = data.get('owner_id')
        self.created_at = datetime.utcnow()
        self.username = data.get('username')
        self.ProfilePic = data.get('ProfilePic')
        self.bio = data.get('bio')

    def __repr__(self):
        return f'<id {self.id}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.utcnow()
        db.session.commit()

    @staticmethod
    def get_one_user(id):
        return ProfileModel.query.filter_by(id=id).first()


class ProfileSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    owner_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    Username = fields.Str(required=True)
    ProfilePic = fields.Str(required=False)
    bio = fields.Str(required=True)
