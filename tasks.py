import os

from invoke import task, run
from slimit import minify as js_minify


@task
def build():

    for filename in os.listdir('app/assets/js'):
        if filename.endswith('.js') and '.min.js' not in filename:
            js_file_path = os.path.join('app/assets/js/', filename)
            min_js_file_path = js_file_path.replace('.js', '.min.js')
            js_file = open(js_file_path)
            min_js_file = open(min_js_file_path, 'w')

            min_js_file.write(
                js_minify(js_file.read(), mangle=True, mangle_toplevel=True)
            )

    run('bower install')
    run('sass --style compressed --update app/assets/css:app/assets/css')
    run('pybabel compile -f -d app/translations')


@task('build')
def start():
    run('./run.py')
