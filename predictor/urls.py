# urls.py

from django.urls import path
from predictor import views

urlpatterns = [
    path('heart/', views.heart, name="heart"),
    path('register/', views.register_patient, name='register_patient'),
    path('prediction/', views.prediction_success, name='prediction_success'),
    # path('prediction_result/', views.prediction_result, name='prediction_result'),  # Add this line
    path('', views.home, name="home"),
]
