"""Intialize Flask app"""
from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config


def init_app():
    """Create Flask application"""
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY
    
    with app.app_context():
        """Importing parts of the application"""
        from .database import initialize_db
        from .routes import register_blueprint
        
        initialize_db(app)
        register_blueprint(app)
        JWTManager(app)

    return app
