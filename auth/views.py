from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect, render
from auth import forms
import auth 
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login as auth_login, 
    logout as auth_logout
)


# Create your views here.

def signup(request):
    signupForm = forms.SignupForm()
    error = None
    if request.method == "POST":
        signupForm = forms.SignupForm(request.POST)
        if signupForm.is_valid():
            username = signupForm.cleaned_data['username']
            password = signupForm.cleaned_data['password']
            first_name = signupForm.cleaned_data['first_name']
            last_name  = signupForm.cleaned_data['last_name']

            confirmPassword = signupForm.cleaned_data['confirmPassword']
            user = User.objects.filter(username = username)
            if password != confirmPassword:
                error = "Password didn't matched"
            elif len(user) != 0:
                error = "Username already exist"
            else:
                user = User.objects.create_user(
                    username = username,
                    password = password,
                    first_name = first_name,
                    last_name = last_name,
                )
                
                auth_login(request,user)
                if request.POST.get('button1') is not None:
                    user.is_staff = True 
                    user.save()
                    return HttpResponseRedirect('/adminhome/')
                
                user.save()
                return HttpResponseRedirect('/userhome/')
    
    context = {
        "form" : signupForm,
        "error" : error
    }
    return render(request,'auth/signup.html',context=context)
            



def login(request):
    loginForm = forms.LoginForm()
    error = None

    if request.method == "POST":
        loginForm = forms.LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            if request.POST.get("button1") is not None:
                user = authenticate(username=username,password=password)
                if user and user.is_staff:
                    auth_login(request,user)
                    return HttpResponseRedirect('/adminhome/')
                else:
                    error = "Credential doesn't matched with admin account"

            else :
                user = authenticate(username = username, password = password)
                if user and user.is_staff == False:
                    auth_login(request,user)
                    return HttpResponseRedirect('/userhome/')
                else:
                    error = "Credential doesn't matched with user account"

    context = {
        "form" : loginForm,
        "error" : error
    }
    return render(request,'auth/login.html',context=context)


def logout(request):
    auth_logout(request)
    return redirect('/auth/login')

@login_required(login_url='/auth/login')
def delete(request,pk):
    user = User.objects.filter(pk = pk).first()
    user.delete()
    return redirect('/adminhome')