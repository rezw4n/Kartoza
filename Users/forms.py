from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'profile_pic', 'home_address', 'phone_number', 'latitude', 'longitude']