#!/usr/bin/python3
"""Flask application."""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns Hello HBNB."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    """Returns C followed by text."""
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
