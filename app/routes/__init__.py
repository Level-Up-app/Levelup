from .Habit.habit import habit_bp

def register_blueprint(app):
    app.register_blueprint(habit_bp)
