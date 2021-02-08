""" Define an Abstract Base Class for models """
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path
import os


env_path = Path('.')
load_dotenv(dotenv_path=env_path)

client = MongoClient(os.getenv("CLIENT_URI"))
mongo = client['levelup_db']


class DBTask:
    def saveTask(self, task):
        pass
    
    def findById(self, task):
        pass

    def getTask(self, task_id):
        pass

    def update(self, query, new_values):
        pass

    def delete(self):
        pass


class MongoClientService(DBTask):
    def __init__(self):
        self.__db = mongo['task']  # db

    def saveTask(self, task):
        if task:
            self.__db.insert_one(task.convert_to_json())
