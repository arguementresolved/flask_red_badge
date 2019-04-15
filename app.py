import os

from src.app import create_app
from flask_heroku import Heroku
from flask_cors import CORS

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)
CORS(app)
heroku = Heroku(app)

if __name__ == '__main__':
    app.run()
