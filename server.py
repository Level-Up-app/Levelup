from flask import Flask, request
import json
from flask_restful import Api
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['MONGO_URI'] = "mongodb://localhost:27017/levelupDB"
mongo = PyMongo(app) # initializing db
api = Api(app) # initializing API



@app.route('/', methods=["GET"])
def get():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
