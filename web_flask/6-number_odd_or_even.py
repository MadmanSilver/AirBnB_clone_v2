#!/usr/bin/python3
""" Starts a flask web app """

from flask import render_template, Flask

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Displays <n> is a number """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """ Displays <n> is a number """
    if n % 2 == 0:
        oe = 'even'
    else:
        oe = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, oe=oe)

if __name__ == '__main__':
    app.run()
