from ..database import db


class Habit(db.Document):
    """Habit Model"""

    title = db.StringField()
    description = db.StringField()
    complete = db.BooleanField()
    created_at = db.DateTimeField()
    # added_by = db.ReferenceField('User')

    def __init__(self, title, description, complete=False, *args, **kwargs):
        super(Habit, self).__init__(*args, **kwargs)
        self.title = title
        self.description = description
        self.complete = complete

    def __repr__(self):
        return 'Habit(title: %r, description: %r, complete: %r)' % (self.title, self.description, self.complete)

    def convert_to_json(self):
        """converts objects into json"""
        return self.__dict__
 