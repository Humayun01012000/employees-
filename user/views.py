from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout  # Needed for login functionality

# Register view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
    else:
        form = UserCreationForm()  # Ensure form is initialized for GET requests

    return render(request, "user/register.html", {"form": form})


# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Authenticate the user
            login(request, user)   # Log the user in
            return redirect('home:employee')
    else:
        form = AuthenticationForm()  # Initialize form for GET requests

    return render(request, "user/login.html", {"form": form})



def logout_view(request):
    if request.user.is_authenticated:  # Check if the user is logged in
        logout(request)  # Log out the user
    return redirect('user:login') 


    

