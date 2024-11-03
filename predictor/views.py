from django.shortcuts import render
import pandas as pd
from xgboost import XGBClassifier
from .forms import PatientRegistrationForm
from .models import Patient
from .models import Prediction

def heart(request):
  if request.method == 'POST':
    # Read the heart disease training data from a CSV file
    df = pd.read_csv('D:\core\predictor\static\cardio_train.csv', delimiter=';')

    # Retrieve user input from the form
    user_data = {
      'age': float(request.POST['age']),
      'gender': request.POST['gender'],
      'height': float(request.POST['height']),
      'weight': float(request.POST['weight']),
      'ap_hi': float(request.POST['ap_hi']),
      'ap_lo': float(request.POST['ap_lo']),
      'cholesterol': float(request.POST['cholesterol']),
      'gluc': float(request.POST['gluc']),
      'smoke': float(request.POST['smoke']),
      'alco': float(request.POST['alco']),
      'active': float(request.POST['active'])
    }

    # Create a DataFrame from the user's data
    user_df = pd.DataFrame([user_data])

    # Add 'gender' column to the DataFrame
    user_df['gender'] = user_data['gender']

    # Convert 'gender' column to categorical type
    user_df['gender'] = user_df['gender'].astype('category')

    # Drop 'id' and 'cardio' columns
    X = df.drop(columns=['id', 'cardio'])
    y = df['cardio']

    # Ensure all values are float type
    X = X.astype(float)
    y = y.astype(float)

    # Initialize and train XGBoost Classifier
    xgb_model = XGBClassifier()
    xgb_model.fit(X, y)

    # Predict using the trained model
    prediction = xgb_model.predict(user_df)

    # Determine prediction result
    if int(prediction[0]) == 1:
      result = 'High Risk'  # User is predicted to have heart disease
    else:
      result = "Low Risk"  # User is predicted to not have heart disease

    context = {
      'user_data': user_data,  # Dictionary containing user input
      'result': result,  # Prediction result
    }
    # Pass the context dictionary to render
    return render(request, 'prediction_result.html', context)

  return render(request, 'heart.html', {'form': PatientRegistrationForm()})

def register_patient(request):
  if request.method == 'POST':
    form = PatientRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request, 'registration_success.html')
  else:
    form = PatientRegistrationForm()
  return render(request, 'register_patient.html', {'form': form})

def prediction_success(request):
  # Retrieve prediction results from the database
  predictions = Prediction.objects.all()
  return render(request, 'prediction_success.html', {'predictions': predictions})


def home(request): 

  return render(request, 

  'home.html') 

def view_patients(request):
  # Retrieve all patients from the database
  patients = Patient.objects.all()
  # Render the template to display a list of patients
  return render(request, 'view_patients.html', {'patients': patients})
