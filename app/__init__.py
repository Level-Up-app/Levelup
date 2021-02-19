"""Intialize Flask app"""
from flask import Flask
from config import Config



def init_app():
    """Create Flask application"""
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)
    # app.config['MONGODB_SETTINGS'] = Config.MONGODB_SETTINGS

    with app.app_context():
        """Importing parts of the application"""
        from .database import initialize_db
        from .routes import register_blueprint
        
        initialize_db(app)
        register_blueprint(app)

    return app
