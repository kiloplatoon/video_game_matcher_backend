from .models import Profile
from django.forms import ModelForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'dob', 'casual_competitive',] 