"""
this is for our website
"""

from flask import Flask , render_template, redirect, url_for

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("base.html")

@app.route("/")
def redirect_to_home():
    return redirect(url_for("home"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/example1")
def show_exanple1():
    return render_template("example1.html")

@app.route("/example2")
def show_exanple2():
    return render_template("example2.html")














if __name__ == "__main__":
    app.run(debug= True)