from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from .models import Child

class CustomAutoForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}))

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label="First Name" ,required=True,help_text='Optional.')
    last_name = forms.CharField(max_length=40,label="Last Name", required=True, help_text='Optional.')
    email = forms.EmailField(max_length=70,required=True,label="Email",help_text='Required. Inform a valid email address.')

    field_order=['username','password1', 'password2', 'first_name', 'last_name', 'email',]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                print field,field_name,field.widget,field.label
                if type(field.widget) in (forms.TextInput, forms.PasswordInput,forms.EmailInput,forms.DateInput):
                    if field_name == 'email':
                        field.widget = forms.TextInput(attrs={'placeholder': "email@address.com",'class':"form-control",})
                    elif field_name == 'passowrd1' or field_name == 'password2':
                        field.widget = forms.PasswordInput(attrs={'placeholder':"Password",'class':'form-control'})
                    else:
                        field.widget = forms.TextInput(attrs={'placeholder': field.label,'class':"form-control",})

    class Meta:
        model = User
        fields ={'username', 'first_name', 'last_name', 'email', 'password1', 'password2',}

    def __str__(self):
        return self.first_name

class ChildRegisterForm(forms.ModelForm):
    age=forms.IntegerField(max_value=20,min_value=1,label="Age" ,required=True)
    field_order=['name','details','age','image',]
    class Meta:
        model = Child
        fields={'name','details','image','age'}
    #function to init the widget with class form-control and a placeholder
    def __init__(self, *args, **kwargs):
        super(ChildRegisterForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            print field.widget
            if field:
                if type(field.widget) in (forms.TextInput, forms.Textarea,forms.NumberInput,forms.ClearableFileInput):
                    if field_name == "name":
                        field.widget = forms.TextInput(attrs={'placeholder': field.label,'class':'form-control'})
                    elif field_name == "details":
                        field.widget = forms.Textarea(attrs={'placeholder': field.label,'class':'form-control'})
                    elif field_name == "image":
                        field.widget = forms.ClearableFileInput(attrs={'placeholder': field.label,'class':'form-control'})
                    elif field_name == "age":
                        field.widget = forms.NumberInput(attrs={'placeholder': field.label,'class':'form-control'})
            print field.widget

    def __str__(self):
        return self.name
