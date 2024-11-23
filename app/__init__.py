from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import logging
import os

# Instantiate necessary components
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'  # Define default login view

def create_app():
    """Factory function to initialize and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configuration from Config class

    # Initialize Flask extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register blueprints for routes and API
    from .routes import main
    from .api import api
    from .notifications import send_notification

    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    # Set up logging
    logging.basicConfig(level=logging.INFO)

    return app
