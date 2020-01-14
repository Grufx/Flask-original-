from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
  return "Hi!dasd"


@app.route('/home')
def home():
  return "<h1><a href='/about'My home</a></h1>"
def about():
  return render_template('about.html')

def contact():
  return render_template('contact.html',Phone=232142)

app.run(host="0.0.0.0",port=8020)