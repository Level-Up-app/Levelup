from flask import jsonify, request
from flask_restful import Resource
from factories import TaskFactory


class TaskResource(Resource):
    def get(self):
        data = request.get_json()
        db = mongo['task']  # db

        task = TaskFactory.create(data['title'], data['description'], False)  # create task object

        if task:
            result = db.insert_one(task.convert_to_json())
            return jsonify({"result": "task created susccessfully"})

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
