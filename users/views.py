from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('all')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('all')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request,'users/login_register.html',{'page':page})

def logoutUser(request):
    logout(request)
    messages.success(request,'User was loggeed out successfully')
    return redirect('login')

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('all')
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"User account was created!")
            login(request,user)
            return redirect('all')
        else:
            messages.success(request,'An error has occured during registration')

    context = {'page':page,'form':form}
    return render(request,'users/login_register.html',context)