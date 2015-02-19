import os
from app import app # from pacckage app imports variable 'app'
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, send_file
from werkzeug import secure_filename
from logic import process_file

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/books', methods=['GET', 'POST'])
def books():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			words = process_file(filename)
			return render_template("books.html", pairs=[word for word in words if len(word[0])>2])
			# return redirect(url_for('uploaded_file',
			# 	filename=filename))
			
	return render_template("books.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_file(os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'], filename))) # NOT flask.send_from_directory()

@app.route('/results/<filename>')
def result_file(filename):
	return send_file(os.path.abspath(os.path.join(app.config['RESULT_FOLDER'], filename)))


@app.route('/movies')
def movies():
	return render_template("movies.html")

@app.route('/songs')
def songs():
	return render_template("songs.html")



# @app.route('/upload_file', methods=['POST', 'GET'])
# def upload_file():
# 	if request.method == 'POST':
# 		file = request.files['file']
# 		if file and allowed_file(file.filename):
# 			filename = secure_filename(file.filename)
# 			# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# 			return redirect(url_for('uploaded_file',
# 				filename=filename))
# 	return 'Bye'