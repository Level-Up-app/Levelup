""" Defines blue print for the tasks """

from flask import Blueprint
from flask_restful import Api
from resources import TaskResource, task_resource

task_blueprint = Blueprint('task', __name__)
Api(task_blueprint).add_resource(TaskResource, '/task')