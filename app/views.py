from datetime import datetime
from uuid import uuid4

from flask import render_template, request, make_response
from app import app, babel


@babel.localeselector
def get_locale():
    if hasattr(request, 'locale'):
        if request.locale in app.config['LOCALES'] and request.locale:
            return request.locale
        else:
            return request.accept_languages.best_match(app.config['LOCALES'])


@app.route('/')
@app.route('/<locale>')
def index_with_locale(locale=None):
    request.locale = locale

    countdown_target = datetime(
        day=12, month=7, year=2014, hour=10, minute=0, second=0
    )

    return render_template('index.html', countdown_to=countdown_target)
