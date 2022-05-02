# https://flask.palletsprojects.com/en/2.1.x/
from flask import Flask, render_template

# Instantiate the Flask Object
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
