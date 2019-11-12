#!/usr/bin/env python3
'''
    example_flask_app.py
    Jeff Ondich, 22 April 2016
    Modified by Eric Alexander, January 2017

    A slightly more complicated Flask sample app than the
    "hello world" app found at http://flask.pocoo.org/.
'''
import flask
from flask import render_template
import json
import sys

app = flask.Flask(__name__)

@app.route('/') #DEFAULT HOMEPAGE
def home():
    return render_template('HomePage.html')


@app.route('/about/') #ABOUT
def about():
    return render_template('aboutpage.html')


@app.route('/comparison/') #COMPARISON, do stuff.
def defaultComparison():
    return render_template('datapage.html')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
