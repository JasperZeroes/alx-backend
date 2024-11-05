#!/usr/bin/env python3
"""A Basic Flask app.
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' Index page'''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
