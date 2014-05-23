from flask import render_template, request
from app import app, babel


@babel.localeselector
def get_locale():
    if hasattr(request, 'locale'):
        return request.locale if request.locale in app.config['LOCALES'] else app.config['DEFAULT_LOCALE']
    return request.accept_languages.best_match(['hu', 'en'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<locale>')
def index_with_locale(locale):
    request.locale = locale
    return render_template('index.html')
