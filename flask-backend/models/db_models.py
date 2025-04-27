from datetime import datetime
from app_configured.configure import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), default='user')  
    password_hash = db.Column(db.String(1024), nullable=False)

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
    connection_info = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    livedata = db.relationship("LiveData", backref="data_source")

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
    live_data = db.relationship("LiveData", backref='metric', lazy=True)
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

class Customers(db.Model):
    __tablename__='customers'
    __table_args__ = {'extend_existing':True}
    id = db.Column(db.Integer , primary_key=True)
    First_Name = db.Column(db.String,nullable=False)
    Last_Name = db.Column(db.String,nullable=False)
    Email = db.Column(db.String,nullable=False)
    Phone = db.Column(db.String,nullable=False)
    status=db.Column(db.String,nullable=False)
    
    def __repr__(self):
        return f"<Customers {self.First_Name}"
    
class Products(db.Model):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing':True}
    id = db.Column(db.Integer,primary_key=True)
    product_name = db.Column(db.String,nullable=False)
    product_catgory=db.Column(db.String,nullable=False)
    Price = db.Column(db.Integer,nullable=False)
    Stock = db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return f"<Product {self.product_name}"
    

class Sales(db.Model):
    __tablename__='sales'
    __table_args__ = {'extend_existing':True}
    id = db.Column(db.Integer,primary_key=True)
    customerid = db.Column(db.Integer,db.ForeignKey('customers.id'))
    productid = db.Column(db.Integer,db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer,nullable=False)
    amount = db.Column(db.Integer,nullable=False)
    date = db.Column(db.Date ,nullable=False)
    status = db.Column(db.String,default='Completed',nullable=False)
    customer = db.relationship('Customers', backref='sales')
    product = db.relationship('Products', backref='sales')

    def __repr__(self):
        return f"<Sales {self.Amount}"
    

class Feature(db.Model):
    __tablename__ = 'features'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    prev_day_revenue = db.Column(db.Float, nullable=False)
    day_of_week = db.Column(db.String(20), nullable=False)
    is_weekend = db.Column(db.Boolean, nullable=False)
    productid = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Feature {self.id}>"