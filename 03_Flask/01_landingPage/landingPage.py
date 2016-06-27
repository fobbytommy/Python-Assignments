from flask import Flask, render_template
app = Flask(__name__)

"""
This one is up to you: I add an additonal '/' after
my routes. This allows the user to navigate to a URL
which either has a trailing backslach or not and still be
taken to the correct page. Without the trailing backslash
included in the route decorator, a user would receive a 404
if they attempted to navigate to '/ninja/' instead of '/ninja'.
"""


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninjas/')
def ninjas():
    return render_template('ninjas.html')


@app.route('/dojos/new/')
def dojos():
    return render_template('dojos.html')

app.run(debug=True)
