#!/usr/bin/python3
"""
This module starts a Flask app
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    returns a greeting when at root/home page
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
