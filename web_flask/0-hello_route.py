#!/usr/bin/python3
"""
Starting Flask Application
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """displays 'Hello HBNB!' on the web browser"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True)
