import json
import os

import flask
from flask import request
from flask_babel import Babel


def translate(filename, source, target, lang):
    full_source = os.path.join(source, filename)
    full_target = os.path.join(target, filename)
    print(f"Processing {full_source} => [{lang}] => {full_target}")
    if not os.path.isdir(target):
        os.makedirs(target)

    # refresh the babel translation
    request.babel_translations = None
    request.babel_locale = lang

    with open(full_source) as f:
        with open(full_target, 'w') as out:
            content = f.read()
            # look for a context file to use
            context_path = os.path.join(source, os.path.splitext(filename)[0], '.ctx.json')
            if os.path.isfile(context_path):
                with open(context_path) as context_file:
                    context = json.load(context_file)
            else:
                context = {}
            output = flask.render_template_string(content, **context)
            # print(output.split("\n")[:5])
            out.write(output)


if __name__ == '__main__':
    app = flask.Flask(__name__, template_folder='')
    app.config.update({'BABEL_TRANSLATION_DIRECTORIES': 'translations'})
    # app.config.from_pyfile('babel.cfg')
    babel = Babel(app, default_locale='it')


    @babel.localeselector
    def get_locale():
        global babel_lang
        print("Now locale is ", babel_lang)
        return babel_lang


    with app.test_request_context():
        translate('index.html', 'template/', '.', lang='it')
        translate('index.html', 'template/', 'en', lang='en')
