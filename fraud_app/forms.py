from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class TransactionForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    merchant_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    transaction_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    transaction_type = forms.ChoiceField(
        choices=[
            ('purchase', 'Purchase'),
            ('refund', 'Refund'),
            ('transfer', 'Transfer'),
            ('withdrawal', 'Withdrawal')
        ],  
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    location = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class FraudReportForm(forms.Form):
    transaction_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    report_type = forms.ChoiceField(
        choices=[
            ('suspicious', 'Suspicious Activity'),
            ('unauthorized', 'Unauthorized Transaction'),
            ('phishing', 'Phishing Attempt'),
            ('other', 'Other')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
    evidence = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

class FeedbackForm(forms.Form):
    transaction_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    was_fraud = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    feedback_notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    confidence_rating = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5})
    )
