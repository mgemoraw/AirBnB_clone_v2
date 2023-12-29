#!/usr/bin/python3
"""
Starting Flask Application
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """displays 'Hello HBNB!' on the web browser"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB at route /hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True)
