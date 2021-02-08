class Task():
    """Task Model"""

    def __init__(self, title, description, complete):
        self.title = title
        self.description = description
        self.complete = complete

    def convert_to_json(self):
        """converts objects into json"""
        return self.__dict__
