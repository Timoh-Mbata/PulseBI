import sys
import os
from flask import Flask , Blueprint, jsonify, request
from flask_jwt_extended import JWTManager
from app_configured.configure import db
from flask_migrate import Migrate
from flask_cors import CORS
from routes.auth_routes import authentification
from routes.metric_routes import metrics_blueprint
from routes.alert_routes import alerts_blueprint
from routes.datasource_routes import dataSource_blueprint
from routes.user_routes import user_routes as user_blueprints
from routes.live_data_routes import liveData_blueprint
from routes.user_dashboard_data_routes import UserDashboardData
from routes.prediction_routes import prediction_blueprint
migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config.from_object("app_configured.configure.Config")  
    db.init_app(app)
    migrate.init_app(app, db)
    jwt = JWTManager(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.register_blueprint(authentification, url_prefix="/auth")
    app.register_blueprint(prediction_blueprint, url_prefix="/prediction")
    app.register_blueprint(metrics_blueprint, url_prefix="/metrics")
    app.register_blueprint(alerts_blueprint, url_prefix="/alerts")
    app.register_blueprint(dataSource_blueprint, url_prefix="/datasource")
    app.register_blueprint(UserDashboardData, url_prefix="/api")
    app.register_blueprint(user_blueprints, url_prefix="/user")
    app.register_blueprint(liveData_blueprint, url_prefix="/api/live_data")
    return app
