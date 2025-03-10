#!/usr/bin/python3
"""
Starts a Flask web application that listens on 0.0.0.0:5000.
It defines a single route "/airbnb-onepage/" that returns "Hello HBNB!".
"""

from flask import Flask

app = Flask(__name__)

@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    """Route handler that returns 'Hello HBNB!' when accessed."""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
