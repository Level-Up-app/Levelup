from .task import task_bp

def register_blueprint(app):
    app.register_blueprint(task_bp)
