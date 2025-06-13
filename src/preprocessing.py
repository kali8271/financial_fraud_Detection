# preprocessing.py
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

def scale_data(X_train, X_test):
    scaler = StandardScaler()
    return scaler.fit_transform(X_train), scaler.transform(X_test)

def balance_data(X, y):
    smote = SMOTE(random_state=42)
    return smote.fit_resample(X, y)
