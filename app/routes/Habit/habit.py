from flask import Blueprint, jsonify, make_response, request, render_template
from json import dumps
from ...models import Habit
from datetime import datetime

habit_bp = Blueprint(
    'habit', __name__, template_folder='templates', static_folder='static'
    )

@habit_bp.route('/habits', methods=["GET"])
def get_all_habits():
    habits = Habit.objects()
    return render_template('habit.html', habits=habits)
    # return jsonify(habits)


@habit_bp.route('/habit', methods=["POST"])
def create_a_habit():
    body = request.get_json()

    if body != None:
        habit = Habit(**body, created_at=datetime.utcnow) # create habit object
        habit.save()
        message = {"result": "habit created susccessfully"}
        return make_response(jsonify(message), 200)
    else:
        message = {"result": "Empty data"}
        return make_response(jsonify(message), 204)


@habit_bp.route('/habit/<habit_id>', methods=['PUT'])
def update_a_habit(habit_id):
    body = request.get_json()
    if body:
        habit = Habit.objects.get(pk=habit_id).update(**body)
        return jsonify({'result': 'habit updated successfully'}), 200

    return jsonify({'result': 'something went wrong'}), 404


@habit_bp.route('/habit/<habit_id>', methods=['DELETE'])
def del_a_habit(habit_id):
    if habit_id:
        habit = Habit.objects.get(pk=habit_id)
        habit.delete()
        return jsonify({'result': 'successfully delete habit'})