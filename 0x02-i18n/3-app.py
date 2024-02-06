#!/usr/bin/env python3
""" script with a single route that output
Welcome to Holberton” as page title """

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ flask app config """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """ function that return the best match
    of our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


home_title = gettext("Welcome to Holberton")
home_header = gettext('Hello world!')


@app.route('/')
def welcome():
    """ returning page '3-index.html '"""
    return render_template('3-index.html',
                           home_title=home_title,
                           home_header=home_header)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
