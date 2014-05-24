import os

from flask import Flask
from flask_redis import Redis
from flask.ext.babel import Babel

# Init app
app = Flask(__name__, static_url_path='/static', static_folder='assets')
try:
    app.config.from_object('config.Config')
except ImportError:  # Assuming Heroku
    app.config.update(
        APP_DIR=os.path.abspath(os.path.dirname(__file__)),
        PROJECT_ROOT=os.path.abspath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), os.pardir)),
        SECRET_KEY=os.urandom(24),
        DEBUG=bool(os.getenv('DEBUG')),
        REDIS_URL=os.getenv('REDISCLOUD_URL'),
        GA_TRACKING_ID='UA-51296526-1',
        GA_DEFAULT_URL='pubstomp.hu',
        LOCALES={'en': 'English', 'hu': 'magyar'},
        DEFAULT_LOCALE='hu',
    )

# Init middleware
redis = Redis(app)
babel = Babel(app)

# Load stuff
from app.views import *
