#!/usr/bin/python3

from flask import Flask
from flask import render_template

host = "http://localhost:8080"

app = Flask(__name__, static_folder="static")

home = open("templates/home.html","r").read()
home = home.replace("HOST",host)
about_content = open("data/about.txt","r").read()

print("Loading files complete")

@app.route('/')
def index():
  return home

@app.route('/about/')
def about_page():
  return render_template('about.html',title="O mně")

app.run(debug=True,host="0.0.0.0",port=8080)

