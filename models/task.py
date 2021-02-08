class Task():
    """Task Model"""

    def __init__(self, _id, title, description, complete):
        self._id = _id
        self.title = title
        self.description = description
        self.complete = complete

    def convert_to_json(self):
        """converts objects into json"""
        return self.__dict__
