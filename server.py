from flask import Flask, render_template, request, jsonify, Blueprint
import json
from flask.helpers import make_response
from flask.wrappers import Request

app = Flask(__name__)
app.config['SECRET_KEY'] = '--s3cret_kEy-'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_image')
def load_image(methods=["POST"]):
	# insert picture here
	return "Success", 200

@app.route('/show_result')
def show_result(methods=["GET"]):
	return render_template('result.html')

def main():
    app.run(port=1234, host="0.0.0.0")
    # 46.146.186.210:1337

if __name__ == "__main__":
    main()
