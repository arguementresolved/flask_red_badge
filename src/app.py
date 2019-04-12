from flask import Flask
from .views.user_view import user_api
from .models import db, bcrypt
from .config import app_config
from flask_cors import CORS
from .views.profile_view import profile_api as profile_blueprint
from .views.user_view import user_api as user_blueprint
from .views.blogpost_view import comment_api as comment_blueprint
from .views.battle_view import battles_api as battles_blueprint

def create_app(env_name):
    '''
    Create App
    '''
    # app initilaztion
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    app.register_blueprint(user_api, url_prefix='/api/v1/users')
    app.register_blueprint(profile_blueprint, url_prefix='/api/v1/profiles')
    app.register_blueprint(comment_blueprint, url_prefix='/api/v1/comments')
    app.register_blueprint(battles_blueprint, url_prefix='/api/v1/battles')

    bcrypt.init_app(app)
    db.init_app(app)

    return app

# @app.route("/profile", methods=['GET', 'POST'])
# @login_required
# def profile():
    # image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

    # return render_template('profile.html', title='Profile', image_file=image_file)
