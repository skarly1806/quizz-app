from flask_cors import CORS
from flask import Flask
from flask import Flask, request
from jwt_utils import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"ouili, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def Login():
	payload = request.get_json()
	if payload == "flask2023":
		token = build_token()
		return token, 200
	else:
		return 'Unauthorized', 401


if __name__ == "__main__":
    app.run()