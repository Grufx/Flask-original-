from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home')
def home():
  return render_template('home.html', aktiva_lapa='home')
  
@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/contact')
def contact():
  return render_template('contact.html',Phone=232142)

@app.route('/params')
def params():
  args= request.args
  return args
  for key. value in args.items():
    print(f"(key).(value)")


@app.route('/post_req')
def post_req()
  return request.args











if __name__=='__main__':
  app.run(host='0.0.0.0',port=8020, threaded = True, debug = True)

