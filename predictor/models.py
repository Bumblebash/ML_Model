from django.db import models

# Create your models here.

# models.py

from django.db import models

class Patient(models.Model):
    # Define choices for gender field
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    # Define choices for smoking status field
    SMOKE_CHOICES = [
        (0, 'No'),
        (1, 'Yes'),
    ]

    # Define choices for alcohol intake status field
    ALCO_CHOICES = [
        (0, 'No'),
        (1, 'Yes'),
    ]

    # Define choices for physical activity level field
    ACTIVE_CHOICES = [
        (0, 'Inactive'),
        (1, 'Active'),
    ]

    # Define choices for cholesterol level field
    CHOLESTEROL_CHOICES = [
        (1, 'Normal'),
        (2, 'Above Normal'),
        (3, 'High'),
    ]

    # Define choices for glucose level field
    GLUC_CHOICES = [
        (1, 'Normal'),
        (2, 'Above Normal'),
        (3, 'High'),
    ]

    # Define fields for Patient model
    # name = models.CharField(max_length=100)  # Name of the patient
    age = models.IntegerField()  # Age of the patient
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)  # Gender of the patient (restricted to Male or Female)
    height = models.IntegerField()  # Height of the patient
    weight = models.FloatField()  # Weight of the patient
    ap_hi = models.IntegerField()  # Systolic blood pressure (ap_hi) of the patient
    ap_lo = models.IntegerField()  # Diastolic blood pressure (ap_lo) of the patient
    cholesterol = models.IntegerField(choices=CHOLESTEROL_CHOICES)  # Cholesterol level of the patient
    gluc = models.IntegerField(choices=GLUC_CHOICES)  # Glucose level of the patient
    smoke = models.IntegerField(choices=SMOKE_CHOICES)  # Smoking status of the patient (0 for non-smoker, 1 for smoker)
    alco = models.IntegerField(choices=ALCO_CHOICES)  # Alcohol intake status of the patient (0 for non-drinker, 1 for drinker)
    active = models.IntegerField(choices=ACTIVE_CHOICES)  # Physical activity level of the patient (0 for inactive, 1 for active)
    prediction_result = models.CharField(max_length=20)  # Add a field to store prediction result
    def __str__(self):
        return self.name

class Prediction(models.Model):
    # Define ForeignKey relationship with Patient model
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  
    # Define field for prediction result
    result = models.CharField(max_length=100)  

    def __str__(self):
        return f"{self.patient.name} - {self.result}"
