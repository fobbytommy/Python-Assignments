from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "JustLikeCollege,WorkNapProcrastinateWorkNap,GoodMorning!"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'wallsdb')
# initial GET route which displays Login & Registration forms
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if request.form['process'] == "login":
		session['login_email'] = request.form['login_email']
		password = request.form['password']
		query = "SELECT * FROM users WHERE email = :email LIMIT 1"
		data = { 'email': str(session['login_email']) }
		user = mysql.query_db(query, data)
		email_find_query = "SELECT COUNT(email) AS count FROM users WHERE email = :email"
		email_data = { 'email': str(session['login_email']) }
		existing_email = mysql.query_db(email_find_query, email_data)
		if existing_email[0]['count'] == 1:
			if bcrypt.check_password_hash(user[0]['pw_hash'], password):
				session['id'] = user[0]['id']
				return redirect('/wall')
			else:
				flash('your password is invalid. Please try again', 'login_error')
				return redirect('/')
		else:
			flash('your email is invalid. Please try again', 'login_error')
			return redirect('/')
	elif request.form['process'] == "register":
		session['first_name'] = request.form['first_name']
		session['last_name'] = request.form['last_name']
		session['register_email'] = request.form['register_email']
		password = request.form['password']
		confirm_password = request.form['confirm_password']
		try:
			email_find_query = "SELECT CASE WHEN email = :email THEN 'True' ELSE 'False' END AS duplicate FROM users"
			email_data = { 'email': str(session['register_email']) }
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
		if len(session['register_email']) < 1:
			errors.append('Your email address cannot be blank.')
		elif not EMAIL_REGEX.match(session['register_email']):
			errors.append('You put an invalid email address.')
		for duplicate_check in email_duplicate:
			if duplicate_check['duplicate'] == 'True':
				errors.append('The email is already in use. Please pick another email.')
				break
		if len(password) < 8:
			errors.append('Your password must be at least 8 characters long.')
		elif password != confirm_password:
			errors.append('Your password does not match the confirmed password.')

		if errors:
			for error in errors:
				flash(error, 'register_error')
			return redirect('/')
		else:
			pw_hash = bcrypt.generate_password_hash(password)
			insert_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
			data = {
						'first_name': str(session['first_name']),
						'last_name': str(session['last_name']),
						'email': str(session['register_email']),
						'pw_hash': pw_hash
					}
			mysql.query_db(insert_query, data)
			select_query = "SELECT id FROM users WHERE email = '{}'".format(str(session['register_email']))
			user = mysql.query_db(select_query)
			session['id'] = user[0]['id']
			return redirect('/wall')

@app.route('/wall')
def wall():
	select_query = "SELECT first_name, id FROM users WHERE id = :id"
	data = { 'id': session['id'] }
	user = mysql.query_db(select_query, data)

	get_messages = "SELECT messages.id, messages.user_id, CONCAT(users.first_name,' ', users.last_name,' - ' ,DATE_FORMAT(messages.created_at, '%M %D %Y %r')) AS name_and_date, messages.message FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
	messages = mysql.query_db(get_messages)

	get_comments = "SELECT comments.id, comments.message_id, comments.user_id, CONCAT(users.first_name,' ', users.last_name,' - ' , DATE_FORMAT(comments.created_at, '%M %D %Y %r')) AS name_and_date, comments.comment FROM comments JOIN users ON comments.user_id = users.id ORDER BY comments.created_at"
	comments = mysql.query_db(get_comments)

	return render_template('wall.html', user = user[0], messages = messages, comments = comments)

@app.route('/log_off', methods=['POST'])
def log_off():
	session.clear()
	return redirect('/')

@app.route('/add_message/<user_id>', methods=['POST'])
def add_message(user_id):
	session['message'] = request.form['message']
	if len(str(session['message'])) < 50:
		flash('Your message is too short! Keep it over 50 characters! That was {}!'.format(len(str(session['message']))))
		return redirect('/wall')
	elif len(str(session['message'])) > 500:
		flash('Your message is too long! Keep it under 500 characters! That was {}!'.format(len(str(session['message']))))
		return redirect('/wall')
	else:
		insert_query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())"
		insert_data = { 'message': str(session['message']), 'user_id': user_id }
		mysql.query_db(insert_query, insert_data)
		session.pop('message')
		return redirect('/wall')

@app.route('/add_comment/<message_id>/<user_id>', methods=['POST'])
def add_comment(message_id, user_id):
	session['comment'] = request.form['comment']
	if len(str(session['comment'])) < 10:
		flash('Your comment is too short! Keep it over 10 characters! That was {}!'.format(len(str(session['comment']))))
		return redirect('/wall')
	elif len(str(session['comment'])) > 500:
		flash('Your comment is too long! Keep it under 500 characters! That was {}!'.format(len(str(session['comment']))))
		return redirect('/wall')
	else:
		insert_query = "INSERT INTO comments (comment, message_id, user_id, created_at, updated_at) VALUES (:comment, :message_id, :user_id, NOW(), NOW())"
		insert_data = { 'comment': str(session['comment']), 'message_id': message_id, 'user_id': user_id }
		mysql.query_db(insert_query, insert_data)
		session.pop('comment')
		return redirect('/wall')

@app.route('/delete_message/<message_id>', methods=['POST'])
def delete_message(message_id):
	check_query = "SELECT id FROM comments where message_id = :message_id"
	data = { 'message_id': message_id }
	check_comments = mysql.query_db(check_query, data)
	if not check_comments:
		delete_query = "SET FOREIGN_KEY_CHECKS=0; DELETE FROM messages WHERE messages.id = :message_id AND DATE_ADD(messages.created_at, INTERVAL 30 MINUTE) > NOW(); SET FOREIGN_KEY_CHECKS=1;"
		mysql.query_db(delete_query, data)
	else:
		delete_query = "SET FOREIGN_KEY_CHECKS=0; DELETE messages, comments FROM messages INNER JOIN comments WHERE messages.id = comments.message_id AND messages.id = :message_id AND DATE_ADD(messages.created_at, INTERVAL 30 MINUTE) > NOW(); SET FOREIGN_KEY_CHECKS=1;"
		mysql.query_db(delete_query, data)
	return redirect('/wall')

@app.route('/delete_comment/<comment_id>', methods=['POST'])
def delete_comment(comment_id):
	delete_query = "SET FOREIGN_KEY_CHECKS=0; DELETE FROM comments WHERE id = :comment_id AND DATE_ADD(created_at, INTERVAL 30 MINUTE) > NOW(); SET FOREIGN_KEY_CHECKS=1;"
	delete_data = { 'comment_id': comment_id }
	mysql.query_db(delete_query, delete_data)
	return redirect('/wall')
app.run(debug=True)
