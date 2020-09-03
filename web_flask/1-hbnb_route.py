#!/usr/bin/python3
""" Starts a flask web app """

from web_flask import app


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays HBNB """
    return 'HBNB'

if __name__ == '__main__':
    app.run()
