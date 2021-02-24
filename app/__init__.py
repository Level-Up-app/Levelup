"""Intialize Flask app"""
from flask import Flask
from config import Config


def init_app():
    """Create Flask application"""
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    with app.app_context():
        """Importing parts of the application"""
        from .database import initialize_db
        from .routes import register_blueprint
        
        initialize_db(app)
        register_blueprint(app)

    return app
