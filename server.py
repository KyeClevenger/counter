from flask import Flask, render_template, redirect, session
app = Flask(__name__)

app.secret_key ="Shhhhh"

@app.route('/')
def index():
	if 'Num' not in session:
		session['Num'] = 0
	session['Num'] += 1
	return render_template('index.html', Num = session['Num'])

@app.route('/double')
def double():
	session['Num'] += 1
	return redirect('/')

@app.route('/reset')
def reset():
	session['Num'] = 0
	return redirect('/')

app.run(debug = True, port=5050)