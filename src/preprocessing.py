# preprocessing.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

def preprocess_data(df):
    """
    Preprocess the transaction data
    
    Args:
        df: DataFrame containing transaction data
        
    Returns:
        X: Preprocessed features
        y: Target variable
    """
    # Separate features and target
    X = df.drop(columns=['is_fraud'])
    y = df['is_fraud']
    
    # Define numeric and categorical columns
    numeric_features = ['amount']
    categorical_features = ['merchant_name', 'transaction_type', 'location']
    
    # Create preprocessing pipelines
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    # Apply preprocessing
    X_processed = preprocessor.fit_transform(X)
    
    # Balance the dataset if needed
    if sum(y == 1) < sum(y == 0) * 0.1:  # If fraud cases are less than 10% of non-fraud
        smote = SMOTE(random_state=42)
        X_processed, y = smote.fit_resample(X_processed, y)
    
    return X_processed, y
