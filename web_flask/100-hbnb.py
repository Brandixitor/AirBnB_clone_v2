#!/usr/bin/python3
""" Starts a Flask application related to HBNB. """

from os import getenv
from flask import Flask, render_template
from models import storage
from models import amenity
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request."""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Flask route at /hbnb.
        Fills the hbnb homepage.
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    values = {"states": states, "amenities": amenities, "places": places}
    return render_template('100-hbnb.html', **values)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
