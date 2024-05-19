from flask import Flask, render_template
import sys

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

@skills_app.route("/python", strict_slashes=False)
def py_def():
        return ("Python is cool")

@skills_app.route("/python/", strict_slashes=False)
def py_defs():
        return ("Python is cool")

@skills_app.route("/python/<text>", strict_slashes=False)
def py_rep(text):
        text = text.replace('_', ' ')
        return ("Python {}".format(text))

@skills_app.route("/number/<int:n>", strict_slashes=False)
def py_num(n):
        return ("{} is a number".format(n))

@skills_app.route("/number_template/<int:n>", strict_slashes=False)
def py_in(n):
        """/number_template/<n>: display a HTML page only if n is an integer"""
        return render_template("5-number.html", n=n)

@skills_app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def py_od(n):
        """/number_odd_or_even/<n>: display a HTML page only if n is an integer"""
        if n % 2 == 0:
                num = "even"
        else:
                num = "odd"
        return render_template("6-number_odd_or_even.html", n=n, num=num)

if __name__ == "__main__":
        skills_app.run(debug=True, host='0.0.0.0', port=5000)
