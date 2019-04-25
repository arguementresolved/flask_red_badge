
import json
from flask import request, g, Blueprint, json, Response
from ..shared.authentication import Auth
from ..models.comments import CommentsModel, CommentsSchema


comment_api = Blueprint('comment_api', __name__)
comments_schema = CommentsSchema()


@comment_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
    req_data = request.get_json()
    req_data['owner_id'] = g.user['id']
    data, error = comments_schema.load(req_data)

    if error:
        print(error)
        return custom_response(error, 404)

    post = CommentsModel(data)
    post.save()

    data = comments_schema.dump(post).data
    return custom_response(data, 201)


@comment_api.route('/<int:id>', methods=['DELETE'])
@Auth.auth_required
def delete(id):

    post = CommentsModel.get_one_comments(id)

    if not post:
        return custom_response({'error': 'post not found'},
                               404)

    data = comments_schema.dump(post).data
    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    post.delete()
    return custom_response({'message': 'deleted'}, 204)


@comment_api.route('/', methods=['GET'])
@Auth.auth_required
def get_all():
    posts = CommentsModel.get_all_comments()
    data = comments_schema.dump(posts, many=True).data
    return custom_response(data, 200)


@comment_api.route('/<int:comments_id>', methods=["GET"])
@Auth.auth_required
def get_one(comments_id):

    post = CommentsModel.get_one_comments(comments_id)

    if not post:
        return custom_response({'error': 'post not found'}, 404)

    data = comments_schema.dump(post).data

    return custom_response(data, 200)


@comment_api.route('/<int:comment_id>', methods=['PUT'])
@Auth.auth_required
def update(comment_id):

    req_data = request.get_json()
    post = CommentsModel.get_one_comments(comment_id)

    if not post:
        return custom_response({'error': 'post not found'}, 404)

    data = comments_schema.dump(post).data

    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    data, error = comments_schema.load(req_data, partial=True)

    if error:
        return custom_response(error, 400)

    post.update(data)
    data = comments_schema.dump(post).data
    return custom_response(data, 200)


def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
