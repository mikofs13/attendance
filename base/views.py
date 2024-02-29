from django.shortcuts import render, redirect
from .models import Permission
from .forms import PermissionForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    context = {
        "user": ""
    }
    print(request.user)
    
    if str(request.user) != "AnonymousUser":
        context["user"] = request.user

    return render(request, 'Home.html', context)


def permission(request):
    if request.user.is_authenticated:
        
        permission = Permission.objects.filter(user=request.user)
        context = {
            "permissions": permission
        }
        return render(request, "list_request.html", context)
    else:
        return redirect("login")

# @login_required
def askPermit(request):
    if request.user.is_authenticated:
        form = PermissionForm()
        if request.method == 'POST':
            form = PermissionForm(request.POST, request.FILES)
            
            if form.is_valid():
                form_sub = form.save(commit=False)
                form_sub.user = request.user
                form_sub.save()
                
                print("success")
                return redirect("permissions-page")
        context = {
            "form": form
        }
        return render(request, "ask_permit.html",context)
    else:
        return redirect("login")
    
    



def register(request):
    if request.method == 'POST':
        # fullname = request.POST["fname"]
        username = request.POST["uname"]
        email = request.POST["email"]
        pass1 = request.POST['pwd']
        cpass = request.POST['cpwd']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")
            
        if User.objects.filter(email=email):
            messages.error(request, "Email already exists")
        
        if cpass == pass1:
            myuser = User.objects.create_user(username=username, email=email, password=pass1)
            myuser.save()
            messages.success(request, "Your account has been succefully Registered")
            redirect("login")
        else:
            messages.error(request, "Passwords doesnt match")
    return render(request, "signin.html")


def loginn(request):
    print("kill1")
    if request.method == 'POST':
        username = request.POST["uname"]
        # email = request.POST["email"]
        password = request.POST['pwd']
        
        user = authenticate(request, username=username, password=password)
        print("all")
        if user is not None:
            login(request=request, user=user)
            print("loggedin")
            return redirect("home")
        else:
            messages.error(request, "Username or password isn'/aren't correct")
            
    return render(request, "login.html")


def logoutt(request):
    logout(request)
    messages.success(request, "Logged out succesfully")
    return redirect("login")