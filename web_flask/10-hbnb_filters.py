#!/usr/bin/python3
""" Starts a Flask application related to HBNB. """

from os import getenv
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
        Flask route at /hbnb_filters.
        Fills the two popovers in hbnb homepage.
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    values = {"states": states, "amenities": amenities}
    return render_template('10-hbnb_filters.html', **values)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
