from flask_mongoengine import MongoEngine
from mongoengine import connect
from mongoengine.connection import DEFAULT_HOST
         
def initialize_db(app):
    db = MongoEngine(app)
    connect('level_up', alias='default')
    

