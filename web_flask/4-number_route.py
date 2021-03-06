#!/usr/bin/python3
""" Starts a flask web app """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ciscool(text):
    """ Displays C <text> """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """ Displays Python <text> """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Displays <n> is a number """
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run()
