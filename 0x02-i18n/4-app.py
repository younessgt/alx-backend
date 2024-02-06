#!/usr/bin/env python3
""" script with a single route that output
Welcome to Holberton” as page title """

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ flask app config """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ function that return the best match
    of our supported languages"""
    user_language = request.args.get('locale')
    if user_language in app.config['LANGUAGES']:
        return user_language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def welcome():
    """ returning page '4-index.html '"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
