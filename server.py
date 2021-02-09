from bson import json_util, ObjectId
from flask import Flask, request, jsonify, Blueprint
from flask_restful import Api
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path
from factories import TaskFactory
from json import dumps
import routes
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
    all_tasks = db.find() # get all tasks from the database

    if len(all_tasks) > 0:
        for task in all_tasks:
            print(task)
    else:
        return jsonify({"result": "No Tasks Available"})

@app.route('/task', methods=["POST"])
def post():
    data = request.get_json()
    db = mongo['task'] # db

    task = TaskFactory.create(data['title'], data['description'], False) # create task object

    if task:
        result = db.insert_one(task.convert_to_json())
        return jsonify({"result": "task created susccessfully"})

@app.route('/task/<task_id>', methods=['PUT'])
def update(task_id):
    db = mongo['task']
    data = request.get_json()

    query = {'_id': ObjectId(task_id)}
    task = TaskFactory(data['title'], data['description'], False)

    new_values = {"$set": task.convert_to_json()}
    result = db.find_one_and_update(query, new_values)

    if result == None:
        return jsonify({'result': 'task does not exist'}), 404

    return dumps(result, default=json_util.default), 200


for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(debug=True)
