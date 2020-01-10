#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import uuid

from flask import Flask, jsonify, flash, request, redirect, make_response
from werkzeug.utils import secure_filename

from app.main.utils import allowed_file
from flask import current_app as app
from . import main


@main.route('/sendfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.content_type):

            filename = secure_filename(file.filename)
            list_dirs = os.listdir(app.config['UPLOAD_FOLDER'])
            while filename in list_dirs:
                filename = str(uuid.uuid4())
            dir = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            os.mkdir(dir)
            filename = filename + ".png"
            save_path = os.path.join(dir, filename)
            file.save(save_path)

            """Deep learning model"""

            x_min = 0
            x_max = 0
            y_min = 0
            y_max = 0
            return jsonify({'x_min': x_min, 'x_max' : x_max, 'y_min' : y_min, 'y_max' : y_max}), 200
        else:
            return "No image found", 400
    if request.method == "GET":
        return "Hello World, my name is Flask"
