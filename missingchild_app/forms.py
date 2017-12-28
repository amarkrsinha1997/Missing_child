from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,help_text='Optional.')
    second_name = forms.CharField(max_length=40, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=70,required=True, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text= 'Required . Format: YYYY-MM-DD')
    phone_number = forms.CharField(max_length=12)
    class Meta:
        model = User
        print User
        fields ={'username', 'first_name', 'second_name', 'email', 'password1', 'password2'}
