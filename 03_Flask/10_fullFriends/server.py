from flask import Flask, render_template, request, session, redirect, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "4thOfJuly,justLikeLastYearAnd2YearsAgo,I'mWorking-_-"
mysql = MySQLConnector(app, 'friendsdb')

# GET route that displays all of the friends on the 'index.html' page
@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends = friends)

# POST route that handles the add friend form submit
# and creates the friend in the DB
@app.route('/friends', methods=['POST'])
def create():
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['occupation'] = request.form['occupation']
	errors = []
	if len(session['first_name']) < 1:
		errors.append("Please put your friend's first name!")
	elif str.isalpha(str(session['first_name'])) == False:
		errors.append("No symbols or numbers are allowed as a first name!")
	if len(session['last_name']) < 1:
		errors.append("Please put your friend's last name!")
	elif str.isalpha(str(session['last_name'])) == False:
		errors.append("No symbols or numbers are allowed as a last name!")
	if len(session['occupation']) < 1:
		errors.append("Please put your friend's occupation!")

	if errors:
		for error in errors:
			flash(error, 'error')
		return redirect('/')
	else:
		query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
		data = {
					'first_name': str(session['first_name']),
					'last_name': str(session['last_name']),
					'occupation': str(session['occupation'])
				}
		mysql.query_db(query, data)
		session.pop('first_name')
		session.pop('last_name')
		session.pop('occupation')
		flash('You have successfully added a friend to the list!', 'success')
		return redirect('/')

# GET route that displays the edit friend page for the particular friend
@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM friends WHERE id = :id"
	data = { 'id': id }
	friend = mysql.query_db(query, data)
	return render_template('edit.html', one_friend = friend[0])

# POST route that handles the edit friend form submitted
# and updates the friend in the DB
@app.route('/friends/<id>', methods=['POST'])
def update(id):
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['occupation'] = request.form['occupation']
	errors = []

	if str.isalpha(str(session['first_name'])) == False and str(session['first_name']) != "":
		errors.append("No symbols or numbers are allowed as a first name!")
	elif len(session['first_name']) > 1:
		query = "UPDATE friends SET first_name = :first_name WHERE id = :id"
		data = { 'first_name': str(session['first_name']), 'id': id}
		mysql.query_db(query, data)
	if str.isalpha(str(session['last_name'])) == False and str(session['last_name']) != "":
		errors.append("No symbols or numbers are allowed as a last name!")
	elif len(session['last_name']) > 1:
		query = "UPDATE friends SET last_name = :last_name WHERE id = :id"
		data = { 'last_name': str(session['last_name']), 'id': id}
		mysql.query_db(query, data)
	if len(session['occupation']) > 1:
		query = "UPDATE friends SET occupation = :occupation WHERE id = :id"
		data = { 'occupation': str(session['occupation']), 'id': id}
		mysql.query_db(query, data)

	if errors:
		for error in errors:
			flash(error, 'error')
		return redirect('/friends/{}/edit'.format(id))
	else:
		session.clear()
		flash("Successfully edited friend's information", 'success')
		return redirect('/')

# POST route that deletes the friend from the DB
@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	query = "DELETE FROM friends WHERE id = :id"
	data = { 'id': id }
	mysql.query_db(query, data)
	flash("Successfully deleted a friend from the list", 'success')
	return redirect('/')

app.run(debug=True)
