from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm, NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def homepage(request):
    return render(request,'home.html')

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/home')
    else:
        form = LoginForm()
    return render(request,'auth/login.html',{'form': form})

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('homepage')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, "auth/register.html", {"form":form})