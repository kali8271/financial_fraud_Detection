import os
import joblib
import numpy as np

def load_model():
    """Load the trained model"""
    try:
        model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'fraud_model.pkl')
        return joblib.load(model_path)
    except Exception as e:
        print(f"Warning: Could not load model: {str(e)}")
        return None

def predict_fraud(features):
    """
    Predict fraud probability for given features
    
    Args:
        features: numpy array of transaction features
        
    Returns:
        float: probability of fraud (0-1)
    """
    model = load_model()
    if model is not None:
        try:
            return model.predict_proba(features)[0][1]  # Return probability of fraud
        except Exception as e:
            print(f"Warning: Model prediction failed: {str(e)}")
    
    # Fallback to a simple rule-based prediction
    amount = features[0][0]
    if amount > 1000:
        return 0.8
    elif amount > 500:
        return 0.6
    else:
        return 0.2

def predict_input(model, input_data):
    return model.predict(input_data), model.predict_proba(input_data)[:, 1]