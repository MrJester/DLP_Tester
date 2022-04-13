import datetime
import os

from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

app.config["FILE_UPLOADS"] = "uploads"


@app.route('/')
def index():
    return render_template('index.htm', title='DLP Tester', active='index')


@app.route('/file', methods=["GET", "POST"])
def file_upload():
    if request.method == "POST":
        if request.files:
            file = request.files["file"]

            now = datetime.datetime.now()

            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print(file)
            file.save(os.path.join(app.config["FILE_UPLOADS"], file.filename))

            return redirect(request.url)
    return render_template('file.htm', title='File Upload', active='file_upload')


@app.route('/text', methods=["GET", "POST"])
def text_submit():
    if request.method == "POST":
        if request.form:
            text_data = request.form["text_data"]

            now = datetime.datetime.now()

            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print(text_data)

            return redirect(request.url)
    return render_template('text.htm', title='Text Submit', active='text_submit')


if __name__ == '__main__':
    app.run()
