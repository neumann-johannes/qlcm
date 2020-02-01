from flask import render_template, jsonify
from app import app
from app.forms import InputForm
import numpy as np

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('index.html', title='Calculate', form=InputForm())

#AJAX
@app.route('/ajax/', methods=['POST'])
def ajax():
	form = InputForm()
	if form.validate_on_submit():
		x = form.x.data
		y = form.y.data
		result = str(np.lcm(x,y)) # calculate & parse to string for jsonify

		return jsonify(result=result)
	return jsonify(result=form.errors)