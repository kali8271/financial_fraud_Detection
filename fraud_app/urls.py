from django.urls import path
from . import views

app_name = 'fraud_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('train-model/', views.train_model, name='train_model'),
]
