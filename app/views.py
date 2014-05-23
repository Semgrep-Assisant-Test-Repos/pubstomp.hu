from flask import render_template, request
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
    return render_template('index.html')


@app.route('/poll', methods=['PUT'])
def submit_poll_response():
    return '', 204
