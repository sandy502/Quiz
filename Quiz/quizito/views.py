from multiprocessing import context
from unicodedata import category
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import *
 

def home(request):
    # if request.user.is_authenticated:
    #     return render(request, 'users/dashboard.html')
    # else:
        return render(request, 'users/home.html')
        # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, 'home.html')

def dashboard(request):
    # # marks = Marks.objects.order_by('score')[:5]
    # if request.user.is_authenticated:
    #     current_user = request.user
    #     user_id = current_user.id
    #     context = {'current_user': current_user,
    #                 'user_id': user_id}
    #     # context = {'marks': 5}
    #     return render(request, 'users/dashboard.html', context)

    if request.method == 'GET':
        category = Category.objects.all()
        context = {'category':category}
    
    return render(request, 'users/dashboard.html', context)

def question(request):

    if request.method == 'GET':
            category = Category.objects.all()
            question = Question.objects.all()
            context = {'category':category,
            'question':question}

    return render(request, 'users/quiz.html', context)    

def signup(request):
 
    if request.user.is_authenticated:
        # return redirect('/home')
        return HttpResponseRedirect('/post/')
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            # return redirect('/home')
            return HttpResponseRedirect('/post/')
         
        else:
            return render(request,'users/signup.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'users/signup.html',{'form':form})
 
 
def signin(request):
    if request.user.is_authenticated:
        # return HttpResponseRedirect('/post/')
        if request.method == 'GET':
            category = Category.objects.all()
            context = {'category':category}
        return render(request, 'users/dashboard.html', context)

    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'users/signin.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                # return HttpResponseRedirect('/post/')
                
                category = Category.objects.all()
                context = {'category':category}
                return render(request, 'users/dashboard.html', context)
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'users/signin.html', {'form': form}) 


   
 
 
def signout(request):
    logout(request)
    return redirect('/quiz/')
    # return HttpResponse('logged out!!!')