""" Defines the Task factory """
from models import Task
from bson import ObjectId

class TaskFactory:

    @staticmethod
    def create(title, description, complete):
        """ create task object """
        return Task(_id=ObjectId(), title=title, description=description, complete=complete)
