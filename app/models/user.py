from ..database.db import db
from mongoengine import EmailField, ReferenceField, PULL, CASCADE
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Document):
    """ User Model """

    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_lenth=6)
    # habits = db.ListField(db.ReferenceField('Habit', reverse_delete_rule=db.Pull))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

# User.register_delete_rule(Habit, 'added_by', db.CASCADE)