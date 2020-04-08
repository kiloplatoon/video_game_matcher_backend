from django import forms
from .models import User, Relationship

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Relationship
        fields = ('user_one', 'user_two', 'status', 'action_user',)