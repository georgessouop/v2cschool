from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import User, Profile
from school.models import School

def signin(request):
    if request.user.is_authenticated:
        # If user is already authenticated, redirect them to dashboard
        return redirect('core:index')
    
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST['username']
        password = request.POST['password']
        
        # Verify user's credentials and returns a User object if the credentials are valid for a backend
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Authentication successful, log the user in. This line creates a sessionId for the user.
            login(request, user)
            return redirect('core:index')  # Redirect to dashboard page after successful login
        else:
            # Authentication failed, display error message
            error_message = "Invalid username or password. Please try again."
            return render(request, 'users/signin.html', {'error_message': error_message})

    return render(request, 'users/signin.html', {})


def signup(request):
    if request.user.is_authenticated:
        # If user is already authenticated, redirect them to dashboard
        return redirect('core:index')
    
    if request.method == 'POST':
        # Retrieve data from the form
        school_name = request.POST.get('school_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Create school
        school_created = School.objects.create(name=school_name) 

        # Create user (superuser)
        user = User.objects.create_superuser(username=username, email=email, password=password, school=school_created)  

        # Create user's profile  
        Profile.objects.create(user=user)
        
        # Redirect to login page
        return redirect('users:signin')

    return render(request, 'users/signup.html', {})


def logout_view(request):
    logout(request)
    return redirect('users:signin')
