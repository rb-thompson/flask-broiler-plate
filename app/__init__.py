from flask import Flask
from .config import Config
# from .extensions import db, migrate
# from .api import api_bp
# from .web import web_bp

# Create Flask app with configuration and extensions
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    # db.init_app(app)
    # migrate.init_app(app, db)

    # Register blueprints
    # app.register_blueprint(api_bp, url_prefix='/api')
    # app.register_blueprint(web_bp)

    return app