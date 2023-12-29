#!/usr/bin/python3
"""
Starting Flask Application
"""
from flask import Flask, render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Returns n if it is integer"""

    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays HTML page only if n is integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
