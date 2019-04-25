from . import db, bcrypt
from datetime import datetime

from marshmallow import fields, Schema


class CommentsModel(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.owner_id = data.get('owner_id')
        self.content = data.get('content')
        self.created_at = datetime.utcnow()
        self.modified_at = datetime.utcnow()

    def __repr__(self):
        return f'<id {self.id}>'

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.utcnow()
        db.session.commit()

    @staticmethod
    def get_all_comments():
        return CommentsModel.query.all()

    @staticmethod
    def get_one_comments(id):
        return CommentsModel.query.get(id)


# models/blog_post.py
class CommentsSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    owner_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
