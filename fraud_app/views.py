import os
import joblib
import numpy as np
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import TransactionForm, FraudReportForm, FeedbackForm

# Load the model (only once)
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'fraud_model.pkl')
model = joblib.load(model_path)

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
            
            # TODO: Add your fraud detection logic here
            # For now, using a simple example
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
            
            # TODO: Add your fraud report processing logic here
            # For example, save to database, notify security team, etc.
            
            messages.success(request, 'Fraud report submitted successfully. Our team will review it shortly.')
            return redirect('home')
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
            
            # TODO: Add your feedback processing logic here
            # For example, update model training data, improve detection accuracy
            
            messages.success(request, 'Thank you for your feedback!')
            return redirect('home')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback.html', {'form': form})

def calculate_risk_score(transaction_data):
    """
    Calculate risk score for a transaction
    This is a placeholder function - replace with your actual risk calculation logic
    """
    # Example risk calculation (replace with your actual logic)
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
