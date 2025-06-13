# data_loader.py
import pandas as pd
from sklearn.model_selection import train_test_split
from src.config import data_path, target_column, test_size, random_state

def load_data():
    return pd.read_csv("data/creditcard.csv")

def split_data(df):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=random_state)
