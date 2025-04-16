# app.py

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app_configured.configure import db
from .creater import create_app
from flask_migrate import Migrate
from .models.db_models import User, DataSource, Metric, LiveData, Alert, Prediction

app = create_app()
migrate = Migrate(app, db)
with app.app_context():
    print("Database connected successfully.")


if __name__ == '__main__':
    app.run(debug=True)
