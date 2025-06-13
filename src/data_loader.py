# data_loader.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os
from src.config import data_path, target_column, test_size, random_state

def load_data():
    """Load data from CSV file or generate sample data if file not found"""
    try:
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'creditcard.csv')
        if os.path.exists(data_path):
            return pd.read_csv(data_path)
        else:
            print("Warning: creditcard.csv not found. Using sample data.")
            return generate_sample_data()
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return generate_sample_data()

def generate_sample_data():
    """Generate sample transaction data for testing"""
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'amount': np.random.uniform(10, 5000, n_samples),
        'merchant_name': [f'Merchant_{i}' for i in range(n_samples)],
        'transaction_type': np.random.choice(['purchase', 'transfer', 'withdrawal', 'deposit'], n_samples),
        'location': [f'Location_{i}' for i in range(n_samples)],
        'is_fraud': np.random.choice([0, 1], n_samples, p=[0.95, 0.05])  # 5% fraud rate
    }
    
    return pd.DataFrame(data)

def split_data(df):
    """Split data into features and target"""
    X = df.drop(columns=['is_fraud'])
    y = df['is_fraud']
    return train_test_split(X, y, test_size=0.2, random_state=42)
