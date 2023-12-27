#!/usr/bin/python3
"""
This module starts a Flask app
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    returns a greeting when at root/home page
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns a greeting when at hbnb page
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    returns 'c' followed text
    """
    return f'C {text.replace("_", " ")}'


@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """
    return 'python' follow by the text argument or
    by 'is cool' by default
    """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """
    returns only an integer
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """
    returns a templete render if argument is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
