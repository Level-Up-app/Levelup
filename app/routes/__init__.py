from .Habit.habit import habit_bp
from .Auth.auth import auth_bp

def register_blueprint(app):
    app.register_blueprint(habit_bp)
    app.register_blueprint(auth_bp)
