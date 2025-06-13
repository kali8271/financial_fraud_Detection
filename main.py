# main.py

from src.data_loader import load_data, split_data
from src.preprocessing import scale_data, balance_data
from src.model_training import get_models
from src.evaluation import evaluate_model
from src.utils import plot_roc_curve

def main():
    # Load and split data
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)

    # Preprocessing
    X_train_scaled, X_test_scaled = scale_data(X_train, X_test)
    X_train_bal, y_train_bal = balance_data(X_train_scaled, y_train)

    # Train and evaluate models
    models = get_models()
    for name, model in models.items():
        print(f"\n=== {name} ===")
        model.fit(X_train_bal, y_train_bal)
        evaluate_model(model, X_test_scaled, y_test)
        plot_roc_curve(model, X_test_scaled, y_test, model_name=name)

if __name__ == "__main__":
    main()