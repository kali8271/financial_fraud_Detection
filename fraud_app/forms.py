from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class TransactionForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'})
    )
    merchant_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter merchant name'})
    )
    transaction_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    transaction_type = forms.ChoiceField(
        choices=[
            ('purchase', 'Purchase'),
            ('transfer', 'Transfer'),
            ('withdrawal', 'Withdrawal'),
            ('deposit', 'Deposit')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    location = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'})
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
