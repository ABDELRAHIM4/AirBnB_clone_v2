#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello HBNB!"


@app.route("/airbnb-onepage/", strict_slashes=False)
def air():
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
