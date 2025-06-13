import os
import joblib
import numpy as np
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import TransactionForm, FraudReportForm, FeedbackForm
from src.model_training import train_models, get_models
from src.predict import predict_fraud
from src.data_loader import load_data
from src.preprocessing import preprocess_data

# Global variable for the model
model = None

def load_model():
    """Load the fraud detection model"""
    global model
    if model is None:
        try:
            model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'fraud_model.pkl')
            model = joblib.load(model_path)
        except Exception as e:
            print(f"Warning: Could not load model: {str(e)}")
            model = None
    return model

def home(request):
    """Home page view with transaction form"""
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # Process transaction data
            transaction_data = {
                'amount': form.cleaned_data['amount'],
                'merchant_name': form.cleaned_data['merchant_name'],
                'transaction_date': form.cleaned_data['transaction_date'],
                'transaction_type': form.cleaned_data['transaction_type'],
                'location': form.cleaned_data['location']
            }
            
            # Calculate risk score
            risk_score = calculate_risk_score(transaction_data)
            is_fraud = risk_score > 0.7  # Example threshold
            
            return render(request, 'transaction_result.html', {
                'transaction': transaction_data,
                'risk_score': risk_score,
                'is_fraud': is_fraud
            })
    else:
        form = TransactionForm()
    
    return render(request, 'home.html', {'form': form})

def report_fraud(request):
    """Handle fraud reporting"""
    if request.method == 'POST':
        form = FraudReportForm(request.POST, request.FILES)
        if form.is_valid():
            # Process fraud report
            report_data = {
                'transaction_id': form.cleaned_data['transaction_id'],
                'report_type': form.cleaned_data['report_type'],
                'description': form.cleaned_data['description'],
                'evidence': form.cleaned_data['evidence']
            }
            
            messages.success(request, 'Fraud report submitted successfully. Our team will review it shortly.')
            return redirect('fraud_app:home')
    else:
        form = FraudReportForm()
    
    return render(request, 'report_fraud.html', {'form': form})

def submit_feedback(request):
    """Handle user feedback on fraud detection results"""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_data = {
                'transaction_id': form.cleaned_data['transaction_id'],
                'was_fraud': form.cleaned_data['was_fraud'],
                'feedback_notes': form.cleaned_data['feedback_notes'],
                'confidence_rating': form.cleaned_data['confidence_rating']
            }
            
            messages.success(request, 'Thank you for your feedback!')
            return redirect('fraud_app:home')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback.html', {'form': form})

def calculate_risk_score(transaction_data):
    """
    Calculate risk score for a transaction using the trained model
    """
    try:
        # Use the src predict module
        features = np.array([[
            float(transaction_data['amount']),
            # Add other features as needed
        ]])
        return predict_fraud(features)
    except Exception as e:
        print(f"Warning: Prediction failed: {str(e)}")
        return calculate_fallback_risk_score(transaction_data)

def calculate_fallback_risk_score(transaction_data):
    """
    Fallback risk calculation when model prediction fails
    """
    base_risk = 0.5
    
    # Adjust risk based on amount
    amount = float(transaction_data['amount'])
    if amount > 1000:
        base_risk += 0.2
    elif amount > 500:
        base_risk += 0.1
    
    # Adjust risk based on transaction type
    if transaction_data['transaction_type'] in ['transfer', 'withdrawal']:
        base_risk += 0.1
    
    # Ensure risk score is between 0 and 1
    return min(max(base_risk, 0), 1)

def get_transaction_history(request):
    """API endpoint to get transaction history"""
    # TODO: Implement actual transaction history retrieval
    # This is a placeholder response
    transactions = [
        {
            'id': '1',
            'amount': 100.00,
            'merchant': 'Example Store',
            'date': '2024-03-20',
            'status': 'completed'
        }
    ]
    return JsonResponse({'transactions': transactions})

def transaction_detail(request, transaction_id):
    """View transaction details"""
    # TODO: Implement actual transaction retrieval from database
    # This is a placeholder response
    transaction = {
        'id': transaction_id,
        'amount': 100.00,
        'merchant': 'Example Store',
        'date': '2024-03-20',
        'status': 'completed',
        'risk_score': 0.3,
        'is_fraud': False
    }
    return render(request, 'transaction_detail.html', {'transaction': transaction})

def get_transaction_detail(request, transaction_id):
    """API endpoint to get transaction details"""
    # TODO: Implement actual transaction retrieval from database
    # This is a placeholder response
    transaction = {
        'id': transaction_id,
        'amount': 100.00,
        'merchant': 'Example Store',
        'date': '2024-03-20',
        'status': 'completed',
        'risk_score': 0.3,
        'is_fraud': False
    }
    return JsonResponse({'transaction': transaction})

def dashboard(request):
    """Dashboard view"""
    return render(request, 'dashboard.html')

def analytics(request):
    """Analytics view"""
    return render(request, 'analytics.html')

def train_model(request):
    """View to handle model training"""
    if request.method == 'POST':
        try:
            # Load and preprocess data
            data = load_data()
            X, y = preprocess_data(data)
            
            # Train models and get the best one
            best_model = train_models(X, y)
            
            # Update the global model
            global model
            model = best_model
            
            messages.success(request, 'Model trained successfully!')
            return redirect('fraud_app:home')
        except Exception as e:
            messages.error(request, f'Error training model: {str(e)}')
            return redirect('fraud_app:home')
    
    return render(request, 'train_model.html', {
        'available_models': list(get_models().keys())
    })

def custom_404(request, exception):
    """Custom 404 error handler"""
    return render(request, '404.html', status=404)

def custom_500(request):
    """Custom 500 error handler"""
    return render(request, '500.html', status=500)
