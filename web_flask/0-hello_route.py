#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
skills_app = Flask(__name__)
@skills_app.route("/")
def hello():
        return "Hello HBNB!"
if __name__ == "__main__":
        skills_app.run(debug=True, host='0.0.0.0', port=5000)
