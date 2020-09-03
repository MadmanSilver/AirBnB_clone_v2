#!/usr/bin/python3
""" Starts a flask web app """

from flask import render_template, Flask
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Displays a list of states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(err):
    """ Closes storage system. """
    storage.close()

if __name__ == '__main__':
    app.run()
