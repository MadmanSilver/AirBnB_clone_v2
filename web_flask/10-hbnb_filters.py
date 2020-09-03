#!/usr/bin/python3
""" Starts a flask web app """

from web_flask import app
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """ Displays filters """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(err):
    """ Closes storage system. """
    storage.close()

if __name__ == '__main__':
    app.run()
