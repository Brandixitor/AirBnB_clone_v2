#!/usr/bin/python3
""" This is the 5th Flask setup script. """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Flask route at root.
        Displays 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Flask route at /hbnb.
        Displays 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
        Flask route at /c/<text>.
        Displays 'C + <text>'.
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
        Flask route at /python/(<text>).
        Displays 'Python + <text>'.
        Default value of <text> : 'is cool'.
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
        Flask route at /number/<n>.
        Displays '<n> + is an number' if <n> is a int.
    """
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
