from flask import render_template, jsonify, request
from app import app
import random
from flask import Flask, render_template, request
from werkzeug import secure_filename
import os.path as op
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   	if request.method == 'POST':
   		f = request.files['file']
   		path = op.join(op.dirname(__file__), 'uploads/', f.filename)
   		f.save(path)
   		return "successful"

@app.route('/cam')
def cam():
    return render_template('cam.html', title='cam')