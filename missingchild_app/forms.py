from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False,help_text='Optional.')
    email = forms.EmailFIeld(max_length=70,required=False, help_text='Required. Inform a valid email address.')
    address = forms.CharField(max_length=200, require=False, help_text='Specify Your Pin and Post Office')

    class Meta:
        model = User
        fields ={'username', 'first_name', 'last_name', 'email','password1','password2',}
        
