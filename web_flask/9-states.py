#!/usr/bin/python3
""" Starts a flask web app """

from web_flask import app
from flask import render_template
from models import storage
from models.state import State


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def show_states(id=None):
    """ Displays a list of states """
    states = storage.all(State)
    if id is not None:
        states = states.get('State.{}'.format(id))
    else:
        states = states.values()
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown_db(err):
    """ Closes storage system. """
    storage.close()

if __name__ == '__main__':
    app.run()
