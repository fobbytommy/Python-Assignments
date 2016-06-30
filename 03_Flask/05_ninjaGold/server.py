from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime
from pytz import timezone
import random

app = Flask(__name__)
app.secret_key = 'Me0w'

def currentTime():
	 western = timezone('America/Los_Angeles')
	 time_now = datetime.now(western)
	 currentTime = time_now.strftime('(%Y/%m/%d %I:%M:%S %p)')
	 return currentTime

class Gold(object):
	def __init__(self):
		self.gold = 0
		self.activities = []
	def farm(self):
		self.made = random.randint(10,20)
		self.gold += self.made
		# currentTime = strftime('(%Y/%m/%d %I:%M %p)', gmtime())
		self.activities.append(['Earned ' + str(ninja.made) + ' golds from the farm! ' + currentTime(), 'green'])
	def cave(self):
		self.made = random.randint(5,10)
		self.gold += self.made
		self.activities.append(['Earned ' + str(ninja.made) + ' golds from the cave! ' + currentTime(), 'green'])
	def house(self):
		self.made = random.randint(2,5)
		self.gold += self.made
		self.activities.append(['Earned ' + str(ninja.made) + ' golds from the house! ' + currentTime(), 'green'])
	def casino(self):
		self.made = random.randint(-50,50)
		self.gold += self.made
		if self.made > 0:
			self.activities.append(['Earned ' + str(ninja.made) + ' golds from the casino! ' + currentTime(), 'green'])
		elif self.made < 0:
			self.activities.append(['Entred a casino and lost ' + str(abs(ninja.made)) + ' golds... Ouch.. ' + currentTime(), 'red'])
		else:
			self.activities.append(['Entred a casino and broke even! Phew..' + currentTime(), 'black'])
	def reset(self):
		self.gold = 0;
		self.activities = []
ninja = Gold()

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def process_money():
	process = request.form['process']
	if process == 'farm':
		ninja.farm()
	elif process == 'cave':
		ninja.cave()
	elif process == 'house':
		ninja.house()
	elif process == 'casino':
		ninja.casino()
	else:
		ninja.reset()
	if ninja.activities:
		ninja.activities.reverse()
		for data in ninja.activities:
			flash(data)
		ninja.activities.reverse()
	session['current_gold'] = ninja.gold;
	return redirect('')
app.run(debug=True)
