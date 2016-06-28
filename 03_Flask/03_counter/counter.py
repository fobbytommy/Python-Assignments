from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

# create object called Counter which has initial attribute called 'count' to 0
class Counter(object):
	def __init__(self):
		self.count = 0
# create instance of Counter object
c = Counter()

@app.route('/')
def index():
	# increment c.count by 1 each time the website is reloaded
	c.count += 1
	session['count'] = c.count
	return render_template('index.html')
@app.route('/ninja/')
def ninja():
	# increment c.count by 1 each time 'Ninja' button is clicked.
	# so this + redirecting = 2
	c.count += 1
	return redirect('/')
@app.route('/hacker/')
def hacker():
	# reset the attribute count of c by 0 each time 'hacker' button is clicked.
	# so this + redirecting = 1
	c.count = 0
	return redirect('/')
app.run(debug=True)
