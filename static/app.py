import os
from src.google_api import call_vision_api
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/pictures'

from werkzeug import secure_filename

### Templates and File Uploading ###

@app.route('/')
def show_home():
	return render_template('home.html')

@app.route('/result', methods = ['POST'])
def show_result():
	if request.method == 'POST':
		f = request.files['pic']
		filename = secure_filename(f.filename) 
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return render_template('result.html', picture=filename)

if __name__ == '__main__':
	# print call_vision_api("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")
	app.debug = True
	app.run(debug=True)



### Hello World ###

'''
@app.route('/')
def helloWorld():
	return 'Hello World!'

@app.route('/hello/<name>')
def hello_world(name):
	return 'Hello %s!' % name

@app.route('/admin')
def hello_admin():
	return 'Hello Adimn'

@app.route('/guest/<guest>')
def hello_guest(guest):
	return 'Hello, guest %s!' % guest

@app.route('/user/<name>')
def hello_user(name):
	if name == 'admin':
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest', guest=name))

################################

### POST Request to Python from HTML ###

@app.route('/success/<name>')
def success(name):
	return "Welcome %s!" % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('success', name=user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('success', name=user))

##########################################
'''