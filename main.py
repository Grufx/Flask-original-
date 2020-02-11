from flask import Flask, render_template, request
from file_proc import read_file, write_file

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


@app.route('/post', methods=['POST'])
def post():
  return request.get.json()

@app.route('/read_file')
def read_from_file():
  content = read_file()
  return content 

@app.route('/write_file', methods = ['POST'])
def write_to_file():
  content_type = request.content_type
  if content_type == 'application/json':
    contentJSON = request.get_json()
    write_file(contentJSON['data'])
    return f"Add line {contentJSON['data']} to file."
  else:
    return f"Content type {content_type} is not supported!"
  
@app.route('/file', methods = ['GET', 'POST'])
def workFile():
  if request.method == 'GET':
    return read_from_file()
  elif request.method == 'POST':
    return write_to_file()
  else:
    return f"Method {request.method} is not supported!"






if __name__=='__main__':
  app.run(host='0.0.0.0',port=25565, threaded = True, debug = True)

