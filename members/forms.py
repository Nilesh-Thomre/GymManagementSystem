from django import forms
from .models import Member
from .models import MemberProfile

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'membership_type']
class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'membership_type': forms.Select(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class WaterIntakeForm(forms.Form):
    WEIGHT_CHOICES = [(i, str(i)) for i in range(30, 151)]  # Range from 30kg to 150kg
    ACTIVITY_LEVEL_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    CLIMATE_CHOICES = [
        ('cool', 'Cool'),
        ('moderate', 'Moderate'),
        ('hot', 'Hot'),
    ]
    
    weight = forms.ChoiceField(choices=WEIGHT_CHOICES, label="Weight (kg)")
    activity_level = forms.ChoiceField(choices=ACTIVITY_LEVEL_CHOICES, label="Activity Level")
    climate = forms.ChoiceField(choices=CLIMATE_CHOICES, label="Climate")
class BodyFatForm(forms.Form):
    weight = forms.FloatField(label='Weight (kg)', min_value=0.1)
    height = forms.FloatField(label='Height (meters)', min_value=0.1)
    age = forms.IntegerField(label='Age', min_value=1)
    gender = forms.ChoiceField(label='Gender', choices=((0, 'Female'), (1, 'Male')))