from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from .models import User, Profile
from school.models import School

# AUTHENTICATION
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
            return render(request, 'users/auth/signin.html', {'error_message': error_message})

    return render(request, 'users/auth/signin.html', {})


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

    return render(request, 'users/auth/signup.html', {})


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:signin')


@login_required
def users_new(request):
    if request.method == 'POST':
        # Retrieve data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        birth_date = request.POST.get('birth_date')
        town = request.POST.get('town')
        neighborhood = request.POST.get('neighborhood')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        # photo = request.POST.get('photo')

        # Verify that required fields are set
        if not first_name or not email or not role or not birth_date or not password or not password_confirm:
            # Rediriger vers le formulaire avec un message d'erreur
            return render(request, 'users/users_new.html', {'error_message': 'Veuillez remplir tous les champs obligatoires'})

        # Verify that passwords match
        if password != password_confirm:
            # Les mots de passe ne correspondent pas, rediriger vers le formulaire avec un message d'erreur
            return render(request, 'users/users_new.html', {'error_message': 'Les mots de passe ne correspondent pas'})


        # Create user
        user = User.objects.create(
            username = first_name,
            first_name = first_name,
            last_name = last_name,
            email = email,
            birth_date = birth_date,
            town = town,
            neighborhood = neighborhood,
            sex = sex,
            phone = phone,
            password = make_password(password),
            school = request.user.school
        ) 

        # Create user's profile
        Profile.objects.create(
            role=role,
            user=user
        )

        return redirect('users:list')


    return render(request, 'users/users_new.html', {})

@login_required
def users_list(request):
    users = User.objects.filter(school=request.user.school).exclude(id=request.user.id)
    return render(request, 'users/users_list.html', {'users': users})