from flask import Blueprint, jsonify, make_response, request
from bson import json_util, ObjectId
from json import dumps
from ..models import Task
from config import Config

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=["GET"])
def get_all_tasks():
    # get all tasks from the database
    all_tasks = Task.objects.get(pk='601fa90a29d0829307f8ec37')
    print(all_tasks)
    return jsonify(all_tasks)
    # if len(all_tasks) > 0:
    #     for task in all_tasks:
    #         print(task)
    # else:
    #     return jsonify({"result": "No Tasks Available"})


@task_bp.route('/task', methods=["POST"])
def post():
    data = request.get_json()

    if data != None:
        task = Task(title=data['title'], description=data['description'], complete=False) # create task object
        task.save()
        message = {"result": "task created susccessfully"}
        return make_response(jsonify(message), 200)
    else:
        message = {"result": "Empty data"}
        return make_response(jsonify(message), 204)


# @task_bp.route('/task/<task_id>', methods=['PUT'])
# def update(task_id):
#     data = request.get_json()

#     query = {'_id': ObjectId(task_id)}
#     task = TaskFactory(data['title'], data['description'], False)

#     new_values = {"$set": task.convert_to_json()}
#     result = db_service.find_one_and_update(query, new_values)

#     if result is None:
#         return jsonify({'result': 'task does not exist'}), 404

#     return dumps(result, default=json_util.default), 200
