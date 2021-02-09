from flask import jsonify, make_response, request
from flask_restful import Resource
from factories import TaskFactory
from db_util import MongoClientService


class TaskResource(Resource):
    def get(self):
        pass

    def post(self):
        data = request.get_json()
        db_service = MongoClientService()

        if data != None:
            task = TaskFactory.create(data['title'], data['description'], False)  # create task object
            db_service.saveTask(task)
            message = {"result": "task created susccessfully"}
            return make_response(jsonify(message), 200)
        else:
            message = {"result": "Empty data"}
            return make_response(jsonify(message), 204)

    def put(self):
        pass

    def delete(self):
        pass
