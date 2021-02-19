from mongoengine.connection import DEFAULT_HOST
from mongoengine.fields import BooleanField, DateField, DateTimeField, StringField
from mongoengine import connect, disconnect, Document
from datetime import datetime


class Task(Document):
    """Task Model"""

    title = StringField()
    description = StringField()
    complete = BooleanField()
    created_at = DateTimeField(default=datetime.utcnow)

    def __init__(self, title, description, complete, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.title = title
        self.description = description
        self.complete = complete

    def __repr__(self):
        return 'Title %r' % (self.title)

    def convert_to_json(self):
        """converts objects into json"""
        return self.__dict__
