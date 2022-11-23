from distutils.filelist import translate_pattern
from application import app, forms
from flask import redirect, render_template, url_for, request, session
from application.forms import MyForm
import secrets
import os

import cv2
import pytesseract
import numpy as np

@app.route("/")
def index():
    return render_template("upload.html", title = "Home Page")

@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":

        sentence = ""

        f = request.files.get("file")
        # something.jpg >> ["something", "jpg"]
        filename, extension = f.filename.split(".")
        generated_filename = secrets.token_hex(20) + f".{extension}"

        file_location= os.path.join(app.config["UPLOADED_PATH"], generated_filename)

        f.save(file_location)

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        img = cv2.imread(file_location)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        boxes = pytesseract.image_to_data(img)

        for i, box in enumerate(boxes.splitlines()):
            if i == 0:
                continue
            box = box.split()

            if len(box) == 12:
                sentence += box[11] + " "

        #print(sentence)

        session["sentence"] = sentence

        return redirect("/decoded/")

    else:
        return render_template("upload.html", title="Upload")

@app.route("/decoded", methods=["POST", "GET"])
def decoded():

    sentence = session.get("sentence")

    form = MyForm()

    if request.method == "POST":
        text_data = form.text_field.data

    else:
        form.text_field.data = sentence
        session["sentence"] = ""
        return render_template("decoded.html", form = form)