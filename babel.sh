#!/usr/bin/env bash
# extract translations
pybabel extract -F babel.cfg -o messages.pot .

# init a language
#pybabel init -i messages.pot -d translations -l en

# update
pybabel update -i messages.pot -d translations
pybabel compile -d translations
