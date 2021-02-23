from ..database import db
from mongoengine.fields import BooleanField, DateField, DateTimeField, StringField
from mongoengine import connect, disconnect
from mongoengine import Document


class Habit(Document):
    """Task Model"""

    title = StringField()
    description = StringField()
    complete = BooleanField()
    created_at = DateTimeField()

    def __init__(self, title, description, complete, *args, **kwargs):
        super(Habit, self).__init__(*args, **kwargs)
        self.title = title
        self.description = description
        self.complete = complete

    def __repr__(self):
        return 'Habit(title: %r, description: %r, complete: %r)' % (self.title, self.description, self.complete)

    def convert_to_json(self):
        """converts objects into json"""
        return self.__dict__
 