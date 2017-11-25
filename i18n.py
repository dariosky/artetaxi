import os

import flask
from flask import request
from flask_babel import Babel

babel_lang = 'it'


def translate(template, lang):
    global babel_lang
    babel_lang = lang

    print(f"Processing {template} => {lang}")
    if not os.path.isdir(lang):
        os.mkdir(lang)
    request.babel_translations = None
    request.babel_locale = lang

    with open(template) as f:
        with open(os.path.join(lang, template), 'w') as out:
            content = f.read()
            output = flask.render_template_string(content)
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
        translate('index.html', 'it')
        translate('index.html', 'en')
