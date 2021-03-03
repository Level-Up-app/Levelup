from flask import Blueprint, jsonify, make_response, request, render_template, redirect
from json import dumps
from ...models import Habit
from datetime import datetime

habit_bp = Blueprint(
    'habit', __name__, template_folder='templates', static_folder='static'
    )

@habit_bp.route('/', methods=['GET'])
def show_habits():
    habits = Habit.objects()
    return render_template('habits.html', habits=habits)

@habit_bp.route('/habits', methods=["GET"])
def get_all_habits():
    habits = Habit.objects()
    # return render_template('habits.html', habits=habits, user="Max")
    return render_template('habits.html', habits=habits, user="Henry")

@habit_bp.route('/habit/<habit_id>', methods=['GET'])
def get_habit(habit_id):
    habit = Habit.objects.get(pk=habit_id)
    return jsonify({'result': habit}) 

@habit_bp.route('/habit', methods=["POST"])
def create_a_habit():
    if request.form['title'] and request.form['description']:
            title = request.form.get('title')
            description = request.form.get('description')
            habit = Habit(title=title, description=description, created_at=datetime.utcnow) # create habit object
            habit.save()
            message = {"result": "habit created susccessfully"}
            return redirect('habits')

    return jsonify({"result": "no form"})

@habit_bp.route('/habit/<habit_id>/edit', methods=['PUT'])
def update_a_habit(habit_id):
    # body = request.get_json()

    print(habit_id)

    # if body:
    #     habit = Habit.objects.get(pk=habit_id).update(**body)
    #     return jsonify({'result': 'habit updated successfully'}), 200

    return jsonify({'result': str(habit_id)}), 200

@habit_bp.route('/habit/<habit_id>', methods=['DELETE'])
def delete_a_habit(habit_id):
    if habit_id:
        habit = Habit.objects.get(pk=habit_id)
        habit.delete()
    return render_template('habits.html', habits=Habit.objects()), 200