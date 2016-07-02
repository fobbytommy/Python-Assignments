from flask import Flask, render_template
app = Flask(__name__)

# initial GET route which renders a default template, 'index.html'
@app.route('/')
def index():
	return render_template('index.html')

# GET route which renders 'ninja.html' template
@app.route('/ninja/')
def ninja():
	# store a value called 'all' to a variable 'ninja'
	return render_template('ninja.html', ninja='all')

# GET route with a placeholder
@app.route('/ninja/<ninja_color>/')
def ninja_color(ninja_color):
	# pass and store any value of an argument to 'ninja'
	# conditional will be done in html using jinja2
	return render_template('ninja.html', ninja=ninja_color)

app.run(debug=True)
