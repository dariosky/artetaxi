#!/bin/env python
import json
import os

import flask
import re
from flask import request
from flask_babel import Babel

SITE = 'https://www.artetaxi.com'


def clean_path(path):
    """ Given a file path return the resource url

        We use it to get the canonical name
    """
    result = re.sub(r'^\.', r'', path)  # remove initial dots
    result = re.sub(r'/index.html$', '/', result)  # final index
    if not result.startswith("/"):  # start with /
        result = "/" + result
    return result


def translate(filename, source, target, locale):
    full_source = os.path.join(source, filename)
    full_target = os.path.join(target, filename)
    print(f"Processing {full_source} => [{locale}] => {full_target}")

    if not os.path.isdir(target):
        os.makedirs(target)

    # refresh the babel translation
    request.babel_translations = None
    request.babel_locale = locale

    with open(full_source) as f:
        with open(full_target, 'w') as out:
            content = f.read()
            # look for a context file to use
            context_path = os.path.join(source, os.path.splitext(filename)[0]) + '.ctx.json'
            if os.path.isfile(context_path):
                with open(context_path) as context_file:
                    context = json.load(context_file)
            else:
                context = {}

            request_path = clean_path(full_target)
            context.update(dict(
                locale=locale,
                request_path=request_path,
                canonical_url=f'{SITE}{request_path}'
            ))

            output = flask.render_template_string(content, **context)
            # print(output.split("\n")[:5])
            out.write(output)


def main():
    app = flask.Flask(__name__, template_folder='template')
    # app.config.update({'BABEL_TRANSLATION_DIRECTORIES': 'translations'})
    Babel(app, default_locale='it')
    with app.test_request_context():
        translate('index.html', 'template/', '.', locale='it')
        for locale in ('en', 'fr', 'pt', 'ru', 'de'):
            translate('index.html', 'template/', locale, locale=locale)

        translate('404.html', 'template/', '.', locale='en')
        translate('500.html', 'template/', '.', locale='en')


if __name__ == '__main__':
    main()
