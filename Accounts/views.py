from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model

Teacher = get_user_model()

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def teacher_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('teacher_home')  # success
        else:
            messages.error(request, 'Invalid email or password')  # failed login

    return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from Accounts.models import Teacher  # Make sure Teacher is imported
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Check if user already exists
        if Teacher.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('signup')

        # Create and save new teacher
        teacher = Teacher.objects.create_user(
            email=email,
            password=password,
            full_name=full_name,
            subject_specialization=subject
        )

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')  # Redirect to login page after signup

    return render(request, 'signup.html')  # Render signup page for GET request



from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def teacher_home(request):
    return render(request, 'school website.html')  # Create this template later




