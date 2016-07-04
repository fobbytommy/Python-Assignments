from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
import re # reg expression
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "iNeedSomeMoney~!"
# establishing connection to the database called 'emailsdb'
mysql =MySQLConnector(app, 'emailsdb')

# initial GET route to render template: 'index.html'
@app.route('/')
def index():
	return render_template('index.html')

# POST route when email address is submitted
@app.route('/process', methods=['POST'])
def process():
	session['email'] = request.form['email']

	# checking email validations:
	# if email address is empty,
	if len(request.form['email']) < 1:
		flash('Email cannot be blank!', 'error')
		return redirect('/')
	# if email doesn't match regular expression,
	# display an "invlaid email address" message.
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid Email Address!', 'error')
		return redirect('/')
	else:
		# add the valid email address to the database
		query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
		data = { 'email': session['email'] }
		mysql.query_db(query, data)
		session['status'] = 'success'
		return redirect('/success')

# GET route to a page that shows the list of emails from the database
@app.route('/success')
def success():
	if session['status'] == 'success':
		flash('The email address you entered {} is a VALID email address! Thank you!'.format(session['email']), 'success')
		# session.pop('email')
	elif session['status'] == 'delete':
		flash('The selected email has been removed from the list! Thank you!', 'delete')
	query = "SELECT id, email, DATE_FORMAT(updated_at, '%m/%d/%y %I:%i %p') AS add_date FROM emails"
	emails = mysql.query_db(query)
	return render_template('success.html', all_emails = emails)

# when delete form is submitted, it will be handled in the route below,
@app.route('/delete_email', methods=['POST'])
def delete():
	query = 'DELETE FROM emails WHERE id = :id' # deleting the email
	data = { 'id': request.form['email_id'] }
	mysql.query_db(query, data)
	session['status'] = 'delete'
	return redirect('/success') # to show the list of emails and success message

# deleting sessions while returning to the main page
@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)
