#!/usr/bin/env python3
""" script with a single route that output
Welcome to Holberton” as page title """

from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions
app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    language = request.args.get('locale')
    if language and (language in app.config['LANGUAGES']):
        return language

    elif g.user:
        user_language = g.user.get('locale')
        if user_language in app.config['LANGUAGES']:
            return user_language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """returnnig the timezone of the user"""
    time_zone = request.args.get('timezone')
    if time_zone:
        try:
            return timezone(time_zone)
        except pytz.exceptions.UnknownTimeZoneError:
            return None

    elif g.user:
        try:
            user_timezone = g.user.get('timezone')
            return timezone(user_timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """ getting the user data """
    user_id = request.args.get('login_as')

    if user_id is not None:
        try:
            key = int(user_id)
            user_dict = users.get(key)
            return user_dict
        except ValueError:
            return None
    return None


@app.before_request
def before_request():
    """ execution get_user function before each request
    and store the returned data (g is special object provided by Flask
     which is unique for each request)"""
    g.user = get_user()


@app.route('/', strict_slashes=False)
def welcome():
    """ returning page '7-index.html '"""
    if g.user:
        username = g.user['name']
    else:
        username = None
    timezone = get_timezone()
    print(type(timezone))
    return render_template('7-index.html', username=username)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
