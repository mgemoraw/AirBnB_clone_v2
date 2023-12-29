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


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """Displays 'C' followed by the value of the text variable"""
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """Displays python + <text> with default 'Python is cool'"""
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
