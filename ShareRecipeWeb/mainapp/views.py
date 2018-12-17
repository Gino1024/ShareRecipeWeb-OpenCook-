from django.shortcuts import render,redirect
from django.http import HttpResponse
from recipe.models import Recipe


from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.

def index(request):
    
    recipes = Recipe.objects.all()
    return render(request,'mainapp/index.html',locals())
def signup(request):
    return render(request,'mainapp/signup.html')
def post_signup(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
   
    user = User.objects.create_user(username,email,password)
    if user:
        return redirect('/',locals())
    else:
        redirect('/signup',locals())
    
    return render(request,'mainapp/index.html')

def post_logout(request):
    auth.logout(request)
    return redirect('/')

def post_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username,password=password)

    if user :
        auth.login(request,user)
        return redirect ('/',locals())
    else:
        return redirect('/',locals())





