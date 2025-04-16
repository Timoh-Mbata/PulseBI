import sys
import os
from flask import Flask
from app_configured.configure import db
from flask_migrate import Migrate

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app_configured.configure.Config")  
    
    # Initialize db and migrate
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app
