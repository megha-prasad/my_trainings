from flask import jsonify,request,flash,render_template,redirect, url_for
result = 0

def home() :
	return render_template('calcu.html')

def addition() :
	if request.method == 'POST' :
		a = request.form["f.no"]
		b = request.form["s.no"]
		result = int(a)+int(b)
		return render_template('addition.html',result=result)
	return render_template('addition.html')

def subtraction() :
	if request.method == 'POST' :
		a = request.form["f.no"]
		b = request.form["s.no"]
		result = int(a)-int(b)
		return render_template('subtraction.html',result=result)
	return render_template('subtraction.html')

def multiplication() :
	if request.method == 'POST' :
		a = request.form["f.no"]
		b = request.form["s.no"]
		result = int(a)*int(b)
		return render_template('multiply.html',result=result)
	return render_template('multiply.html')

def division() :
	if request.method == 'POST' :
		a = request.form["f.no"]
		b = request.form["s.no"]
		result = int(a)/int(b)
		return render_template('division.html',result=result)
	return render_template('division.html')