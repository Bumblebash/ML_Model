from django import forms

class HeartDiseaseForm(forms.Form):
	# Define form fields for heart disease prediction
 
    id  = forms.FloatField(label='id', widget=forms.NumberInput(attrs={'class': 'form-control'})) 
    # Field for , represented as a float input widget
    
    age = forms.FloatField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for age, represented as a float input widget

    gender = forms.FloatField(label='gender', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for sex, represented as a float input widget

    height = forms.FloatField(label='height', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for chest pain type (CP), represented as a float input widget

    weight = forms.FloatField(label='weight', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for resting blood pressure (TRESTBPS), represented as a float input widget

    ap_hi = forms.FloatField(label='ap_hi', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for serum cholesterol level (CHOL), represented as a float input widget

    ap_lo = forms.FloatField(label='ap_lo', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for fasting blood sugar (FBS), represented as a float input widget

    cholesterol= forms.FloatField(label='CHOL', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for resting electrocardiographic results (RESTECG), represented as a float input widget

    gluc = forms.FloatField(label='gluc', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for maximum heart rate achieved (THALACH), represented as a float input widget

    smoke = forms.FloatField(label='smoke', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for exercise-induced angina (EXANG), represented as a float input widget

    alco = forms.FloatField(label='alco', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for ST depression induced by exercise relative to rest (OLDPEAK), represented as a float input widget

    active = forms.FloatField(label='active', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for the slope of the peak exercise ST segment (SLOPE), represented as a float input widget

    cardio = forms.FloatField(label='cardio', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for the number of major vessels colored by fluoroscopy (CA), represented as a float input widget

	# thal = forms.FloatField(label='THAL', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# Field for thalassemia (THAL), represented as a float input widget
