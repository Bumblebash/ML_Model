#imported all library
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from predictor.forms import  HeartDiseaseForm

from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from predictor.forms import HeartDiseaseForm


def heart(request):
	# Read the heart disease training data from a CSV file
	df = pd.read_csv('D:/core/static/cardio_train.csv')
	data = df.values
	X = data[:, :-1] # Input features (all columns except the last one)
	Y = data[:, -1:] # Target variable (last column)

		# Ensure that Y is a 1-dimensional array
	Y = Y.ravel()


	value = ''

	if request.method == 'POST':
		# Retrieve the user input from the form
		id = float(request.POST['id'])
		age = float(request.POST['age'])
		gender = float(request.POST['gender'])
		height = float(request.POST['height'])
		weight = float(request.POST['weight'])
		ap_hi = float(request.POST['ap_hi'])
		ap_lo = float(request.POST['ap_lo'])
		cholesterol = float(request.POST['cholesterol'])
		gluc = float(request.POST['gluc'])
		smoke = float(request.POST['smoke'])
		alco = float(request.POST['alco'])
		active = float(request.POST['active'])
		cardio = float(request.POST['cardio'])
		

		# Create a numpy array with the user's data
		user_data = np.array(
			(id,
			age,
	        gender,
			height,
			weight,
			ap_hi,
			ap_lo,
			cholesterol,
			gluc,
			smoke,
			alco,
			active,
			cardio)
			
		).reshape(1, 13)

		# Create and train a Random Forest Classifier model
		rf = RandomForestClassifier(
			n_estimators=16,
			criterion='entropy',
			max_depth=9
		)

		rf.fit(np.nan_to_num(X), Y) # Train the model using the training data
		rf.score(np.nan_to_num(X), Y) # Evaluate the model's accuracy
		# print("Request data:", request.data)
		predictions = rf.predict(user_data) # Make predictions on the user's data

		if int(predictions[0]) == 1:
			value = 'have' # User is predicted to have heart disease
		elif int(predictions[0]) == 0:
			value = "don\'t have" # User is predicted to not have heart disease

	return render(request,
				'heart.html',
				{
					'context': value,
					'title': 'Heart Disease Prediction',
					'active': 'btn btn-success peach-gradient text-white',
					'heart': True,
					'form': HeartDiseaseForm(),
				})


def home(request):
	return render(request,
				'home.html')
