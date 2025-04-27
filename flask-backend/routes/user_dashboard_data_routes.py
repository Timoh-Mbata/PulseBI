from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import func, extract
from datetime import datetime, timedelta
from app_configured.configure import db 
from models.db_models import Sales, Prediction, Customers, Products  # Use consistent names

UserDashboardData = Blueprint('user_dashboard_data', __name__)

@UserDashboardData.route('/user_dashboard_data', methods=['GET'])
def get_user_dashboard_data():

    # Total sales (count of sales records)
    total_sales = db.session.query(func.count(Sales.id)).scalar()

    # Get the latest prediction
    latest_prediction = db.session.query(Prediction)\
        .order_by(Prediction.prediction_date.desc())\
        .first()

    if latest_prediction:
        revenue_forecasted = latest_prediction.predicted_value
    else:
        revenue_forecasted = None  # No prediction found

    # Fix: active_customers needs .scalar() to become integer
    active_customers = db.session.query(func.count(Customers.id))\
        .filter(Customers.status == 'Active')\
        .scalar()

    # Top 3 Products by sales quantity
    top_products = db.session.query(
        Products.product_name,
        func.sum(Sales.quantity).label('sales')
    ).join(Sales, Sales.productid == Products.id) \
     .group_by(Products.product_name) \
     .order_by(func.sum(Sales.quantity).desc()) \
     .limit(3).all()

    top_products_list = [{'product_name': product_name, 'sales': sales} for product_name, sales in top_products]

    # Sales Trends - total sales per weekday
    sales_trends_raw = db.session.query(
        extract('dow', Sales.date).label('weekday'),  # Dow: 0=Sunday, 6=Saturday
        func.sum(Sales.amount).label('amount')
    ).group_by('weekday').all()

    weekday_map = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    sales_trends = {weekday_map[int(weekday)]: amount for weekday, amount in sales_trends_raw}

    # Customers activity in last 4 hours
    try:
        from models.db_models import Activity
        four_hours_ago = datetime.utcnow() - timedelta(hours=4)
        recent_activities = db.session.query(Activity).filter(Activity.timestamp >= four_hours_ago).all()

        customer_activities = {
            f'customer{idx+1}': {
                'activity': act.action,
                'timestamp': act.timestamp.isoformat()
            } for idx, act in enumerate(recent_activities)
        }
    except ImportError:
        customer_activities = {}
    
    user_data = {
        'dashboard_data': {
            'Total sales': total_sales or 0,
            'Revenue Forecasted': round(revenue_forecasted,2) or 0,
            'Active Customers': active_customers or 0,
            'Top Products': top_products_list,
            'Sales Trends': sales_trends,
            'customers last 4 hours activity': customer_activities
        }
    }

    return jsonify(user_data), 200
