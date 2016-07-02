from flask import Flask, render_template, session, redirect, request, flash
import re
import time
# a regular expression object for checking valid email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "INeedAJob!80k+<3"

# default GET route to render 'index.html'
@app.route('/')
def index():
	return render_template('index.html')

# POST route when the form is submitted by the user
@app.route('/process', methods=['POST'])
def process():
	# store all form values to the sessions whether the values are
	# valid or not. This avoids user to retype all form information again
	# (see <script> tag in 'index.html')
	session['email'] = request.form['email']
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['birthday'] = request.form['birthday']
	session['password'] = request.form['password']
	session['confirm_password'] = request.form['confirm_password']

	errors = [] # empty list for storing possible errors

	# if email is empty,
	if len(session['email']) < 1:
		errors.append('Please put your email address!')
	# if email does not meet the 'XXXX@xxx.xxx' set by regex expression,
	elif not EMAIL_REGEX.match(request.form['email']):
		errors.append('Invalid Email Address!')
	# if first_name is empty,
	if len(session['first_name']) < 1:
		errors.append('Please put your first name!')
	# if first_name contains symbol(s) or numberic value(s),
	elif str.isalpha(str(session['first_name'])) == False:
		errors.append('Your first name cannot contain symbol(s) or number(s)!')
	# if last_name is empty,
	if len(session['last_name']) < 1:
		errors.append('Please put your last name!')
	# if last_name contains symbol(s) or numberic value(s),
	elif str.isalpha(str(session['last_name'])) == False:
		errors.append('Your first name cannot contain symbol(s) or number(s)!')
	try:
		# if users birthday is in the future,
		if time.strptime(str(session['birthday']), "%Y-%m-%d") > time.localtime():
			errors.append('Stop watching Back to the Future!')
	# if python gets an error, Date of Birth contains non-number information.
	except:
		errors.append('Please put numbers for your Date of Birth.')
	# if password is empty,
	if len(session['password']) < 1:
		errors.append('Please put your password!')
	# if password is less than 8 characters,
	elif len(session['password']) < 8:
		errors.append('Your password must be more than 8 characters!')
	# if password does not have at least 1 uppercase letter OR
	# does not have at least 1 nurmeric value,
	elif sum(1 for c in str(session['password']) if c.isupper()) < 1 or bool(re.search(r'\d',str(session['password']))) == False:
		errors.append('Your password must have at least 1 upper case letter and 1 numeric value!')
	# if password does not match with the confirm password,
	elif session['password'] != session['confirm_password']:
		errors.append('Your passward does not match with the confirmed password!')

	# if there are any errors, show those errors to users
	if errors:
		for error in errors:
			flash(error, 'error')
		return redirect('/')
	# if no errors, automatically reset.
	else:
		return redirect('/reset')

# reset route to clear the valid forms and tell user a confirmation notice.
@app.route('/reset')
def reset():
	session.clear() # delete all current sessions
	# tell the user with a confirmation.
	flash('Thanks for submitting your information.', 'success')
	return redirect('/')

app.run(debug=True)
