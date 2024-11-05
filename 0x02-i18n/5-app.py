#!/usr/bin/env python3
"""A Basic Flask app.
"""
from flask import Flask, render_template, request, g
from typing import Union, Dict
from flask_babel import Babel

app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    '''Retrieves a user based on a user id.
    '''
    login_id = request.args.get('login_as')
    return users.get(int(login_id), None)


@app.before_request
def before_request() -> None:
    ''' Performs some routines before each request's resolution.
    '''
    user = get_user()
    g.user = user


class Config():
    ''' Class to set Babels default locale and timezone'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Use the Config class to set default locale and timezone
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    ''' Determine the best match with our supported languages
    '''
    if locale in request.args and\
            request.args.get('locale', None) in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' Index page'''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
