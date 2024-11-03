from django import forms
from predictor.models import Patient

class HeartDiseaseForm(forms.Form):
    # Age field: Input for age in years
    age = forms.FloatField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    # Gender field: Dropdown menu for selecting gender
    gender = forms.ChoiceField(label='Gender', choices=[(1, 'Male'), (2, 'Female')], widget=forms.Select(attrs={'class': 'form-control'}))
    
    # Height field: Input for height in centimeters (cm)
    height = forms.FloatField(label='Height (cm)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    # Weight field: Input for weight in kilograms (kg)
    weight = forms.FloatField(label='Weight (kg)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    # Systolic Blood Pressure (ap_hi) field: Input for systolic blood pressure in mmHg
    ap_hi = forms.FloatField(label='Systolic Blood Pressure (mmHg)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    # Diastolic Blood Pressure (ap_lo) field: Input for diastolic blood pressure in mmHg
    ap_lo = forms.FloatField(label='Diastolic Blood Pressure (mmHg)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    # Cholesterol Level field: Dropdown menu for selecting cholesterol level
    cholesterol = forms.ChoiceField(label='Cholesterol Level', choices=[(1, 'Normal'), (2, 'Above Normal'), (3, 'Well Above Normal')], widget=forms.Select(attrs={'class': 'form-control'}))
    
    # Glucose Level field: Dropdown menu for selecting glucose level
    gluc = forms.ChoiceField(label='Glucose Level', choices=[(1, 'Normal'), (2, 'Above Normal'), (3, 'Well Above Normal')], widget=forms.Select(attrs={'class': 'form-control'}))
    
    # Smoking Status field: Dropdown menu for selecting smoking status
    smoke = forms.ChoiceField(label='Smoking Status', choices=[(0, 'No'), (1, 'Yes')], widget=forms.Select(attrs={'class': 'form-control'}))
    
    # Alcohol Consumption field: Dropdown menu for selecting alcohol consumption status
    alco = forms.ChoiceField(label='Alcohol Consumption', choices=[(0, 'No'), (1, 'Yes')], widget=forms.Select(attrs={'class': 'form-control'}))
    
    # Physical Activity Level field: Dropdown menu for selecting physical activity level
    active = forms.ChoiceField(label='Physical Activity Level', choices=[(0, 'Inactive'), (1, 'Active')], widget=forms.Select(attrs={'class': 'form-control'}))


# Patient Registration Form

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        # Specify the fields to include in the form
        fields = ['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']

        # Define labels for form fields
        labels = {
            'age': 'Age',
            'gender': 'Gender',
            'height': 'Height (cm)',
            'weight': 'Weight (kg)',
            'ap_hi': 'Systolic Blood Pressure (mmHg)',
            'ap_lo': 'Diastolic Blood Pressure (mmHg)',
            'cholesterol': 'Cholesterol Level',
            'gluc': 'Glucose Level',
            'smoke': 'Smoking Status',
            'alco': 'Alcohol Intake Status',
            'active': 'Physical Activity Level',
        }

        # Define widgets to customize form field appearance
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'ap_hi': forms.NumberInput(attrs={'class': 'form-control'}),
            'ap_lo': forms.NumberInput(attrs={'class': 'form-control'}),
            'cholesterol': forms.Select(attrs={'class': 'form-control'}),
            'gluc': forms.Select(attrs={'class': 'form-control'}),
            'smoke': forms.Select(attrs={'class': 'form-control'}),
            'alco': forms.Select(attrs={'class': 'form-control'}),
            'active': forms.Select(attrs={'class': 'form-control'}),
        }
