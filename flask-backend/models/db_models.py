from datetime import datetime
from app_configured.configure import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"



#Data Source Table
class DataSource(db.Model):
    __tablename__ = 'data_sources'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    live_data = db.relationship('LiveData', backref='data_source', lazy=True)

    def __repr__(self):
        return f"<DataSource {self.name}>"


# Metrics Table
class Metric(db.Model):
    __tablename__ = 'metrics'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text)
    live_data = db.relationship('LiveData', backref='metric', lazy=True)
    alerts = db.relationship('Alert', backref='metric', lazy=True)

    def __repr__(self):
        return f"<Metric {self.name}>"


#Live Data Table
class LiveData(db.Model):
    __tablename__ = 'live_data'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    metric_id = db.Column(db.Integer, db.ForeignKey('metrics.id'), nullable=False)
    datasource_id = db.Column(db.Integer, db.ForeignKey('data_sources.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    metric_value = db.Column(db.Float, nullable=False)
    region = db.Column(db.String(100))

    def __repr__(self):
        return f"<LiveData {self.metric_value} at {self.timestamp}>"


# prediction Table
class Prediction(db.Model):
    __tablename__ = 'predictions'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(100), nullable=False)
    input_reference = db.Column(db.String(255))
    predicted_value = db.Column(db.Float, nullable=False)
    confidence_score = db.Column(db.Float)
    prediction_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Prediction {self.model_name} - {self.predicted_value}>"


#Alerts Table
class Alert(db.Model):
    __tablename__ = 'alerts'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    metric_id = db.Column(db.Integer, db.ForeignKey('metrics.id'), nullable=False)
    condition = db.Column(db.String(5), nullable=False)
    threshold = db.Column(db.Float, nullable=False)
    alert_message = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Alert {self.alert_message}>"
