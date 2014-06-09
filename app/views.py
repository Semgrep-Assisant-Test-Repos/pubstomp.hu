from uuid import uuid4

from flask import render_template, request, make_response
from app import app, babel, redis


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
    response = make_response(render_template('index.html'))
    if 'u' not in request.cookies:
        response.set_cookie('u', str(uuid4())[:13])
    return response


@app.route('/poll', methods=['PUT'])
def submit_poll_response():
    if 'u' in request.cookies:
        redis.set(request.cookies['u'], request.form['value'])
        return '', 204
    else:
        return '', 400
