from django import forms
from .models import programme

class StudentRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    programme = forms.ModelChoiceField(
        queryset=programme.objects.all(),  # Get all Programme instances
        widget=forms.Select
    )
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    aadhaar_number = forms.CharField(max_length=12)
    email_id = forms.EmailField(max_length=100)
    guardian = forms.CharField(max_length=100)
    guardian_number = forms.CharField(max_length=15)
    
    VEG = 'Veg'
    NON_VEG = 'Non-Veg'
    FOOD_CHOICES = [
        (VEG, 'Vegetarian'),
        (NON_VEG, 'Non-Vegetarian'),
    ]
    food_preference = forms.ChoiceField(choices=FOOD_CHOICES, widget=forms.RadioSelect)
    user_name = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)