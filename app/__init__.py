import os

from flask import Flask
from flask_redis import Redis

from app.views import init_views


def create_app():
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
        )

    app.redis_store = Redis(app)

    init_views(app)
    return app
