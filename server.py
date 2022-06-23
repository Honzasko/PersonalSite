#!/usr/bin/python3

from flask import Flask
from flask import render_template


app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
  return render_template("home.html")

@app.route('/about/')
def about_page():
  return render_template('about.html',title="O mně")

@app.route("/social/")
def social_page():
    return render_template("social.html",title="Socialní sítě")

app.run(host="0.0.0.0")

