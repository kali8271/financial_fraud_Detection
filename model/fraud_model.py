import numpy as np
from sklearn.ensemble import RandomForestClassifier

class FraudDetectionModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        
    def predict(self, features):
        """
        Make a prediction for a single transaction
        features: array-like of shape (n_features,)
        """
        # For development, return random predictions
        return np.random.choice([0, 1], p=[0.95, 0.05])  # 95% legitimate, 5% fraud
        
    def predict_proba(self, features):
        """
        Get probability estimates for a single transaction
        features: array-like of shape (n_features,)
        """
        # For development, return random probabilities
        prob = np.random.random()
        return np.array([1 - prob, prob])  # [prob_legitimate, prob_fraud]

# Create and save the model
if __name__ == "__main__":
    model = FraudDetectionModel()
    import joblib
    joblib.dump(model, 'fraud_model.pkl') 