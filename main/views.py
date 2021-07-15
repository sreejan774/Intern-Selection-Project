from auth.views import login
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/auth/login')
def userhome(request):
    context = {}
    return render(request,'main/userhome.html',context=context)

@login_required(login_url='/auth/login')
def adminhome(request):

    users = User.objects.filter(is_staff = False)
    
    context = {
        "users" : users
    }
    return render(request,'main/adminhome.html',context=context)


