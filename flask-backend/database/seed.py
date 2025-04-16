from datetime import datetime
from ..app_configured.configure import Config, db  # Relative import
from ..creater import create_app
from ..models.db_models import User, DataSource, Metric, LiveData, Prediction, Alert

app = create_app()

with app.app_context():
    db.drop_all()  # Drop all tables
    db.create_all()  # Create all tables

    # 👤 Users
    admin = User(username="admin", email="admin@pulsebi.com", role="admin", password_hash="hashed_admin_password")
    jane = User(username="analyst_jane", email="jane@pulsebi.com", role="analyst", password_hash="hashed_jane_password")

    # 📡 Data Sources
    pos = DataSource(name="POS System", type="Retail", description="Retail sales from physical stores")
    web = DataSource(name="Website Analytics", type="Web", description="Traffic and conversion from site")

    # 📊 Metrics
    sales = Metric(name="Total_Sales", unit="KSh", description="Total revenue from POS")
    conversion = Metric(name="Conversion_Rate", unit="%", description="Website conversion percentage")
    cart = Metric(name="Cart_Abandonment", unit="%", description="Users who abandon their carts")

    db.session.add_all([admin, jane, pos, web, sales, conversion, cart])
    db.session.commit()  # Commit to get IDs for metrics and data sources

    # 📈 Live Data
    live_entries = [
        LiveData(metric_id=sales.id, datasource_id=pos.id, timestamp=datetime(2025, 4, 15, 9), metric_value=120000, region="Nairobi"),
        LiveData(metric_id=sales.id, datasource_id=pos.id, timestamp=datetime(2025, 4, 15, 10), metric_value=145000, region="Nairobi"),
        LiveData(metric_id=conversion.id, datasource_id=web.id, timestamp=datetime(2025, 4, 15, 10), metric_value=4.2, region="Web")
    ]
    db.session.add_all(live_entries)

    # 🔮 Predictions
    prediction_entries = [
        Prediction(model_name="Sales Forecast v1", input_reference="Last 7 days", predicted_value=158000, confidence_score=0.89, prediction_date=datetime(2025, 4, 15, 12)),
        Prediction(model_name="Cart Abandonment Trend", input_reference="Web Analytics", predicted_value=12.5, confidence_score=0.91, prediction_date=datetime(2025, 4, 15, 12))
    ]
    db.session.add_all(prediction_entries)

    # 🚨 Alerts
    alerts = [
        Alert(metric_id=sales.id, condition="<", threshold=100000, alert_message="⚠️ Sales have dropped below 100K!", is_active=True),
        Alert(metric_id=cart.id, condition=">", threshold=15, alert_message="⚠️ Cart abandonment rate is too high!", is_active=True)
    ]
    db.session.add_all(alerts)

    db.session.commit()  # Commit all entries into the database
    print("✅ Seed data successfully loaded into the database!")
