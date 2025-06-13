# src/model_training.py

import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.svm import SVC

from src.evaluation import evaluate_model


def get_models():
    """
    Returns a dictionary of classification models to be trained and evaluated.
    """
    return {
        "Logistic Regression": LogisticRegression(max_iter=500),
        "Random Forest": RandomForestClassifier(n_estimators=100),
        "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss'),
        "LightGBM": LGBMClassifier(),
        "SVC": SVC(probability=True)
    }


def train_models(X, y):
    """
    Trains multiple models, evaluates them, and saves the best one to a .pkl file.

    Parameters:
        X: Features (DataFrame or ndarray)
        y: Target labels

    Returns:
        best_model: Trained model with highest ROC AUC score
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = get_models()

    best_score = 0
    best_model = None
    best_model_name = ""

    for name, model in models.items():
        print(f"\n🔍 Training {name}...")
        model.fit(X_train, y_train)
        score = evaluate_model(model, X_test, y_test)

        if score > best_score:
            best_score = score
            best_model = model
            best_model_name = name

    print(f"\n✅ Best model: {best_model_name} with ROC AUC: {best_score:.4f}")

    # Save the best model to models/ folder
    joblib.dump(best_model, 'models/best_model.pkl')
    print("📦 Model saved as models/best_model.pkl")

    return best_model
