#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
skills_app = Flask(__name__)
@skills_app.route("/", strict_slashes=False)
def hello():
        return ("Hello HBNB!")
@skills_app.route("/hbnb", strict_slashes=False)
def hb():
        return ("HBNB")
@skills_app.route("/c/<text>", strict_slashes=False)
def c_rep(text):
	text = text.replace('_', ' ')
	return ("C {}".format(text))
if __name__ == "__main__":
        skills_app.run(debug=True, host='0.0.0.0', port=5000)
