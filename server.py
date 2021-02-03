from flask import Flask, request, jsonify
from flask_restful import Api
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['MONGO_URI'] = "mongodb://localhost:27017/levelupDB"
mongo = PyMongo(app) # initializing db
api = Api(app) # initializing API


class Task():
    """Task Model"""
    
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

    def convert_to_json(self):
        """converts objects into json"""
        return self.__dict__



@app.route('/', methods=["GET"])
def get():
    db = mongo['task']
    all_tasks = db.find() # get all tasks from mongo

    if len(all_tasks) > 0:
        for task in all_tasks:
            print(task)
    else:
        return jsonify({"result": "No Tasks Available"})

@app.route('/task', methods=["POST"])
def post():
    data = request.get_json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)