from flask import render_template, jsonify, request
from app import app, models, db
import random

from flask import request, flash, get_flashed_messages

from flask import Flask, render_template, request
from werkzeug import secure_filename
import os.path as op
import os
import base64
from hashlib import md5
from time import localtime
from flask_login import current_user

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

def convert_and_save(b64_string):
    b64_string = b64_string[22:]
    missing_padding = len(b64_string) % 4
    if missing_padding != 0:
        b64_string += str(b'='* (4 - missing_padding))

    name = md5(str(localtime()).encode('utf-8')).hexdigest()+'.png'
    path = op.join(op.dirname(__file__), 'uploads/', name)
    with open(path, "wb") as fh:
           fh.write(base64.decodebytes(str.encode(b64_string)))
    return name

@app.route('/cam', methods = ['GET','POST'])
def cam():
    if (request.method=="POST"):
        print("test")
        f = request.form['file']
        name = convert_and_save(f)
        userid = current_user.get_id()
        cate = request.form["cate"]

        p = models.Picture(
            user_id=userid, 
            tag=cate, 
            image_path=name, 
            verified=None
        )
        db.session.add(p)
        db.session.commit()
    return render_template('cam.html', title='Cam')

@app.route('/label_task', methods = ['GET', 'POST'])
def label():

    # retrieve the image from the database
    # op.join(op.dirname(__file__), 'uploads/', f.filename)
    img_addr = "static/img/logo.jpg"
    category = 'Green box'

    if request.method == 'POST':
        if request.form['isCorrect'] == 'Yes':
            verified_res = True
        else:
            verified_res = False

        # update the database

        # retrieve the image from the database
        img_addr = "static/img/logo.jpg"
        category = 'Green box'

        return render_template('label_task.html', img_addr = img_addr, category = category)

    return render_template('label_task.html', img_addr = img_addr, category = category)
