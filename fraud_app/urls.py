from django.urls import path
from . import views

app_name = 'fraud_app'

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('report/', views.report_fraud, name='report_fraud'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),
    
    # Transaction related
    path('transaction/<str:transaction_id>/', views.transaction_detail, name='transaction_detail'),
    path('transaction/<str:transaction_id>/report/', views.report_fraud, name='report_specific_fraud'),
    path('transaction/<str:transaction_id>/feedback/', views.submit_feedback, name='submit_specific_feedback'),
    
    # API endpoints
    path('api/transactions/', views.get_transaction_history, name='transaction_history'),
    path('api/transactions/<str:transaction_id>/', views.get_transaction_detail, name='api_transaction_detail'),
    path('api/risk-score/', views.calculate_risk_score, name='api_risk_score'),
    
    # Dashboard and Analytics
    path('dashboard/', views.dashboard, name='dashboard'),
    path('analytics/', views.analytics, name='analytics'),
    
    # Error pages
    path('404/', views.handler404, name='404'),
    path('500/', views.handler500, name='500'),
]
