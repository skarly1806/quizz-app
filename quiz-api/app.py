from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"ouili, {x}"

if __name__ == "__main__":
    app.run()