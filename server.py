from flask import Flask, render_template, request, jsonify, Blueprint
import json
import os
from flask.helpers import make_response
from flask.wrappers import Request
from img2 import Editor
from PIL import Image
from werkzeug.utils import secure_filename


CLIENT_LANG = 'ru'
IMAGE_PATH = "./static/img/sample.jpg"
UPLOAD_FOLDER = os.path.join('static', 'img')
THEME = 'dark'

editor = Editor()
im = ''
app = Flask(__name__)
app.config['SECRET_KEY'] = '--s3cret_kEy-'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=['POST', 'GET'])
def index():
    global CLIENT_LANG, UPLOAD_FOLDER, THEME, IMAGE_PATH
    if request.method == 'GET':
        ss = editor.return_palette(IMAGE_PATH)
        params = {
            'image': IMAGE_PATH,
            'colors': ss
        }
        if CLIENT_LANG == 'ru':
            return render_template('index.html', **params)
        else:
            return render_template('index_en.html', **params)
    elif request.method == 'POST':
        f = request.files['file']

        # print(f.read())
        im = f
        ss = editor.return_palette(im)
        # ss = []
        filename = secure_filename(f.filename)
        print(f)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        IMAGE_PATH = './static/img/' + filename
        print(IMAGE_PATH)
        params = {
            'colors': ss, 
            'image': IMAGE_PATH
        }
        if CLIENT_LANG == 'ru':
            return render_template('index.html', **params)
        else:
            return render_template('index_en.html', **params)


@app.route('/change_language', methods=['POST'])
def change_language():
    global CLIENT_LANG
    data = json.loads(request.form['data'])
    CLIENT_LANG = data
    return 'Data received', 200


@app.route('/theme', methods=["GET", "POST"])
def change_theme():
    global THEME
    if request.method == 'GET':
        return THEME, 200
    if request.method == 'POST':
        data = json.loads(request.form['data'])
        THEME = data
        print(THEME)
        return 'Data received', 200


def main():
    app.run(port=1234, host="0.0.0.0")
    # 46.146.186.210:1337


if __name__ == "__main__":
    main()
