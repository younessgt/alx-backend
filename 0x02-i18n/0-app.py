#!/usr/bin/env python3
""" script with a single route that output
Welcome to Holberton” as page title """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    """ returning welcome to Holberton"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
