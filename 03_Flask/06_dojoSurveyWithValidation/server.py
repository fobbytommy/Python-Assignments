from flask import Flask, render_template, redirect, session, request, flash
app = Flask(__name__)
app.secret_key = 'HeyWutSupSon'

# initial GET route to a survey
@app.route('/')
def index():
	return render_template('index.html')

# form processor
@app.route('/process', methods=['post'])
def process():
	# store the data in sessions regardless of the invalidation
	# to avoid retyping the ones that are valid already.
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']

	errors = [] # for storing possible invalidations

	# if the user did not specify a 'name' at all,
	if len(session['name']) < 1:
		errors.append('Please add your name.')
	# if the user did not choose any 'location',
	if len(session['location']) < 1:
		errors.append('Please choose your location.')
	# if the user did not choose any 'language',
	if len(session['language']) < 1:
		errors.append('Please choose your favoriate language.')
	# if the user did not specify a 'comment' at all,
	if len(session['comment']) < 1:
		errors.append('Please add some comments.')
	# if the user put more than 120 characters in 'comment',
	if len(session['comment']) > 120:
		errors.append('Please keep the comment under 120 characters.')

	# if we have any invalidation, send user back to the survery form
	# with errors showing on the page (see template: 'index.html')
	if errors:
		for error in errors:
			flash(error)
		return redirect('/')
	# if there are no invalidations, go to the result page
	else:
		return redirect('/result/')

@app.route('/result/')
def user_info():
	return render_template('result.html')

@app.route('/reset', methods=['post'])
def reset():
	session.clear() # delete all current sessions
	return redirect('/')

app.run(debug = True)
