from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, ChildRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Child
import pdb

def home(request):
    #pdb.set_trace()
    child = Child.objects.all()[:10]
    print Child.objects.values('image')
    return render(request, "home.html",{'child':child})

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def upload(request):
    #pdb.set_trace()
    if request.method=="POST":
        form = ChildRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ChildRegisterForm()
        return render(request,'upload.html',{'form':form})
