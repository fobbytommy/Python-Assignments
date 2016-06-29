from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Yolo"

class randomNum(object):
	def __init__(self):
		self.number = 0
	def pickRandom(self):
		self.number = random.randrange(0, 101)
r = randomNum()
r.pickRandom()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
	session['randomNum'] = r.number
	session['guess'] = int(request.form['guess']) # convert to int
	if session['guess'] > session['randomNum']:
		session['optionNum'] = 1 # when 'guess' is greater than randomNum
	elif session['guess'] < session['randomNum']:
	 	session['optionNum'] = 2 # when 'guess' is less than randomNum
	else:
		session['optionNum'] = 3 # when 'guess' is equal to randomNum
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['optionNum'] = 4 # to trigger statements in 'else' clause
	r.pickRandom() # invoking a function called 'pickRandom()' to reassign a
				   # randomNum
	return redirect('/')

app.run(debug=True)
