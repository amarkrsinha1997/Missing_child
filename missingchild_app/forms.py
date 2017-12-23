from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=70,required=False, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text= 'Required . Format: YYYY-MM-DD')
    phone_number = forms.IntegerField(help_text= 'Enter your phone number with country code')
    pass

    class Meta:
        model = User
        fields ={'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date'}
