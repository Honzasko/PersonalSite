#!/usr/bin/python3

from flask import Flask
from flask import render_template,redirect,request
from flask_mobility import Mobility

import config
import languages

config.load_Config("settings.cfg")


languages.InitLangs()

def LangExist(lang):
  index = 0
  for i in languages.allowed_langs:
    if i == lang:
      return index
    index += 1
  return -1

app = Flask(__name__, static_folder="static")
Mobility(app)

@app.route('/<lang>/')
def index(lang):
  index = 0
  if LangExist(lang) != -1:
    index = LangExist(lang)
  else:
    return "Error 500"

  return render_template("home.html",object=languages.langs[index],lang=lang)


@app.route('/')
def redir_index():
  lang = request.accept_languages.best_match(languages.allowed_langs)
  return redirect(lang + "/")

@app.route('/<lang>/about/')
def about_page(lang):
  index = 0
  if LangExist(lang) != -1:
    index = LangExist(lang)
  else:
    return "Error 500"
  return render_template('about.html',object=languages.langs[index],title=languages.langs[index].title_about_me)

@app.route('/about/')
def redir_about():
  lang = request.accept_languages.best_match(languages.allowed_langs)
  return redirect(lang + "/about/")

@app.route("/<lang>/social/")
def social_page(lang):
  index = 0
  if LangExist(lang) != -1:
    index = LangExist(lang)
  else:
    return "Error 500"
  return render_template("social.html",object=languages.langs[index],title=languages.langs[index].title_social)
  
@app.route('/social/')
def redir_social():
  lang = request.accept_languages.best_match(languages.allowed_langs)
  return redirect(lang + "/social/")    
  
if config.server_port == 0:
  config.server_port = 5000


app.run(host="0.0.0.0",port=config.server_port)