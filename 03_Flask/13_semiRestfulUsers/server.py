from flask import Flask, render_template, request, session, flash, redirect
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "LetsFinishThisFastSoICanGoRun5damnMilesWEEEE"
mysql = MySQLConnector(app, 'usersdb')

@app.route('/')
def index():
	return redirect ('/users/')

@app.route('/users/')
def users():
	session.clear()
	select_query = "SELECT id, CONCAT_WS(' ', first_name, last_name) AS full_name, email, DATE_FORMAT(created_at, '%M %D, %Y') AS created_date FROM users"
	users = mysql.query_db(select_query)
	return render_template('users.html', users = users)

@app.route('/users/new/')
def new():
	return render_template('new.html')

@app.route('/users/create', methods=['POST'])
def create():
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['email'] = request.form['email']
	try:
		email_find_query = "SELECT CASE WHEN email = :email THEN 'True' ELSE 'False' END AS duplicate FROM users"
		email_data = { 'email': str(session['email']) }
		email_duplicate = mysql.query_db(email_find_query, email_data)
	except:
		pass
	errors = []
	if len(session['first_name']) < 2:
		errors.append('Your first name must be at least 2 characters long.')
	elif str.isalpha(str(session['first_name'])) == False:
		errors.append('Your first name cannot contain symbols or numbers.')
	if len(session['last_name']) < 2:
		errors.append('Your last name must be at least 2 characters long.')
	elif str.isalpha(str(session['last_name'])) == False:
		errors.append('Your last name cannot contain symbols or numbers.')
	if len(session['email']) < 1:
		errors.append('Your email address cannot be blank.')
	elif not EMAIL_REGEX.match(session['email']):
		errors.append('You put an invalid email address.')
	for duplicate_check in email_duplicate:
		if duplicate_check['duplicate'] == 'True':
			errors.append('The email is already in use. Please pick another email.')
			break
	if errors:
		for error in errors:
			flash(error)
		return redirect('/users/new/')
	else:
		insert_query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
		data = {
					'first_name': str(session['first_name']),
					'last_name': str(session['last_name']),
					'email': str(session['email'])
				}
		mysql.query_db(insert_query, data)
		session.clear()
		return redirect('/users/')

@app.route('/users/<id>/')
def show(id):
	select_query = "SELECT id, CONCAT_WS(' ', first_name, last_name) AS full_name, email, DATE_FORMAT(created_at, '%M %D, %Y') AS created_date FROM users WHERE id = :id"
	data = { 'id': id}
	one_user = mysql.query_db(select_query, data)
	return render_template('show.html', user = one_user[0] )

@app.route('/users/<id>/edit/')
def edit(id):
	select_query = "SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, '%M %D, %Y') AS created_date FROM users WHERE id = :id"
	data = { 'id': id }
	one_user = mysql.query_db(select_query, data)
	return render_template('edit.html', user = one_user[0] )

@app.route('/users/<id>/update', methods=['POST'])
def update(id):
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['email'] = request.form['email']
	try:
		email_find_query = "SELECT CASE WHEN email = :email THEN 'True' ELSE 'False' END AS duplicate FROM users"
		email_data = { 'email': str(session['email']) }
		email_duplicate = mysql.query_db(email_find_query, email_data)
	except:
		pass
	errors = []
	if str.isalpha(str(session['first_name'])) == False and str(session['first_name']) != "":
		errors.append("No symbols or numbers are allowed as a first name!")
	elif len(session['first_name']) < 2 and str(session['first_name']) != "":
		errors.append('New first name must be at least 2 characters long.')
	if str.isalpha(str(session['last_name'])) == False and str(session['last_name']) != "":
		errors.append("No symbols or numbers are allowed as a last name!")
	elif len(session['last_name']) < 2 and str(session['last_name']) != "":
		errors.append('New last name must be at least 2 characters long.')
	if str(session['email']) != "":
		if not EMAIL_REGEX.match(session['email']):
			errors.append('You put an invalid email address.')
		for duplicate_check in email_duplicate:
			if duplicate_check['duplicate'] == 'True':
				errors.append('The email is already in use. Please pick another email.')
				break

	if errors:
		for error in errors:
			flash(error)
		return redirect('/users/{}/edit/'.format(id))
	else:
		if len(session['first_name']) > 1:
			query = "UPDATE users SET first_name = :first_name, updated_at = NOW() WHERE id = :id"
			data = { 'first_name': str(session['first_name']), 'id': id}
			mysql.query_db(query, data)
		if len(session['last_name']) > 1:
			query = "UPDATE users SET last_name = :last_name, updated_at = NOW() WHERE id = :id"
			data = { 'last_name': str(session['last_name']), 'id': id}
			mysql.query_db(query, data)
		if len(session['email']) > 1:
			query = "UPDATE users SET email = :email, updated_at = NOW()  WHERE id = :id"
			data = { 'email': str(session['email']), 'id': id}
			mysql.query_db(query, data)
		session.clear()
		flash("Successfully edited user's information")
		return redirect('/users/{}/'.format(id))

@app.route('/users/<id>/destroy', methods=['POST'])
def delete(id):
	delete_query = "DELETE FROM users WHERE id = :id"
	data = { 'id': id }
	mysql.query_db(delete_query, data)
	return redirect('/users/')

app.run(debug=True)
