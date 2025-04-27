from flask import Blueprint, request, jsonify
from app_configured.configure import db
import os
import onnxruntime as rt
import numpy as np
from datetime import datetime
from models.db_models import Prediction, Feature ,Sales
import joblib as jbl
import pandas as pd
from datetime import datetime, timedelta

prediction_blueprint = Blueprint('prediction_blueprint', __name__)

# Correct model path
model_path = os.path.join(os.path.dirname(__file__), '..', 'services', 'Revenue-Models', 'RevuePrediction_RandomForest_Model.onnx')
model_path = os.path.abspath(model_path)

# Load ONNX model session
sess = rt.InferenceSession(model_path, providers=['CPUExecutionProvider'])
input_name = sess.get_inputs()[0].name

# Prediction function
def make_prediction(features):
    input_array = np.array(features).astype(np.float32)  # np.float -> np.float32 (correct)
    input_array = input_array.reshape(1, -1)
    preds = sess.run(None, {input_name: input_array})
    predicted_value = preds[0][0][0]
    confidence_score = 0.85  # Static for now
    return predicted_value, confidence_score

# Endpoint: Predict and store prediction
@prediction_blueprint.route('/predict-storage-api', methods=['POST'])
def predict_and_store():
    try:
        # Fetch the latest feature record
        latest_feature = db.session.query(Feature).order_by(Feature.id.desc()).first()
        if not latest_feature:
            return jsonify({'error': 'No feature data found in database'}), 404

        features = [
            latest_feature.prev_day_revenue,
            latest_feature.day_of_week,
            latest_feature.is_weekend,
            latest_feature.productid,
            latest_feature.quantity
        ]

        # Perform prediction
        predicted_value, confidence_score = make_prediction(features)

        # 🛠️ Fix: Cast to native Python float
        predicted_value = float(predicted_value)
        confidence_score = float(confidence_score)

        # Save prediction result into database
        new_prediction = Prediction(
            model_name="PulseBi 24hrs Revenue Prediction",
            input_reference="Latest Features",
            predicted_value=predicted_value,
            confidence_score=confidence_score,
            prediction_date=datetime.now()
        )
        db.session.add(new_prediction)
        db.session.commit()

        return jsonify({
            'message': 'Prediction successful and saved',
            'predicted_value': predicted_value,
            'confidence_score': confidence_score
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    finally:
        db.session.close()

# Endpoint: Get all predictions
@prediction_blueprint.route('/predicted-revenue-api', methods=['GET'])
def get_all_predictions():
    try:
        predictions = Prediction.query.order_by(Prediction.prediction_date.desc()).all()

        prediction_list = [{
            'id': pred.id,
            'model_name': pred.model_name,
            'input_reference': pred.input_reference,
            'predicted_value': pred.predicted_value,
            'confidence_score': pred.confidence_score,
            'prediction_date': pred.prediction_date.strftime('%Y-%m-%d %H:%M:%S')
        } for pred in predictions]

        return jsonify(prediction_list), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        db.session.close()



# Endpoint: Get the latest prediction
@prediction_blueprint.route('/latest-predicted-revenue-api', methods=['GET'])
def get_latest_prediction():
    try:
        latest_prediction = Prediction.query.order_by(Prediction.prediction_date.desc()).first()

        if not latest_prediction:
            return jsonify({'error': 'No predictions found'}), 404

        prediction_data = {
            'id': latest_prediction.id,
            'model_name': latest_prediction.model_name,
            'input_reference': latest_prediction.input_reference,
            'predicted_value': round(latest_prediction.predicted_value, 2),
            'confidence_score': latest_prediction.confidence_score,
            'prediction_date': latest_prediction.prediction_date.strftime('%Y-%m-%d %H:%M:%S')
        }

        return jsonify(prediction_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        db.session.close()


@prediction_blueprint.route('/predicted-nextweek-sales-Trend-api', methods=['POST','GET'])
def get_next_week_sales_trend():
    try:
        model_path = os.path.join(os.path.dirname(__file__), '..', 'services', 'Sales-Trends Model', 'Sales-Trend-Predictor-Model.pkl')
        model_path = os.path.abspath(model_path)
        model = jbl.load(model_path)

        features = Sales.query.all()
        if not features:
            return jsonify({'error': 'No feature data found in database'}), 404
        
        sales_data = []
        for feature in features:
            sales_data.append({
                'date': feature.date,  
                'amount': feature.amount
            })
        
        # Convert to pandas DataFrame for better handling
        df = pd.DataFrame(sales_data)
        df['date'] = pd.to_datetime(df['date'])  
        df.set_index('date', inplace=True)  

        sales_series = df['amount']

        forecast = model.forecast(steps=7)  

        
        predicted_sales = forecast.tolist()

        return jsonify({
            'predicted_sales_next_week': predicted_sales,
            'message': 'Sales predicted for next week.'
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

        