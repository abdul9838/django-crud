from django import forms
from .models import User

class UserDetail(forms.ModelForm):
    class Meta:
        model = User 
        fields = '__all__' 
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
