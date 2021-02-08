from bson import json_util, ObjectId
from flask import Flask, request, jsonify
from flask_restful import Api
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path
from models import Task
import json
import os

env_path = Path('.')
load_dotenv(dotenv_path=env_path)

app = Flask(__name__, template_folder='templates', static_folder='static')
client = MongoClient(os.getenv("CLIENT_URI"))
mongo = client['levelup_db']
api = Api(app) # initializing API


@app.route('/', methods=["GET"])
def get():
    db = mongo['task']
    all_tasks = db.find() # get all tasks from mongo

    if len(all_tasks) > 0:
        for task in all_tasks:
            print(task)
    else:
        return jsonify({"result": "No Tasks Available"})

@app.route('/task', methods=["POST"])
def post():
    data = request.get_json()
    db = mongo['task'] # db
    task = Task(title=data['title'], description=data['description'], complete=False) # create task object

    if task:
        result = db.insert_one(task.convert_to_json())
        return jsonify({"result": "task created susccessfully"})


if __name__ == '__main__':
    app.run(debug=True)
