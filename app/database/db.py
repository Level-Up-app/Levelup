from flask_mongoengine import MongoEngine
from mongoengine import connect
from mongoengine.connection import disconnect
         
db = MongoEngine()

def initialize_db(app):
    db.init_app(app)
    
    

