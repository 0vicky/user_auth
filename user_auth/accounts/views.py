from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserSelectionForm, PatientCreationForm, DoctorCreationForm
from .models import Patient, Doctor
from django.http import HttpResponseRedirect

def signup(request):
    if request.method == 'POST':
        user_selection_form = UserSelectionForm(request.POST)
        if user_selection_form.is_valid():
            user_type = user_selection_form.cleaned_data.get('user_type')
            if user_type == 'patient':
                return redirect(reverse('accounts:patient_signup'))
            elif user_type == 'doctor':
                return redirect(reverse('accounts:doctor_signup'))
    else:
        user_selection_form = UserSelectionForm()

    context = {
        'user_selection_form': user_selection_form
    }
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/accounts/profile')  # Replace with the desired URL
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'accounts/login.html')


def patient_signup(request):
    if request.method == 'POST':
        form = PatientCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Redirect to the patient dashboard or any desired page
            return redirect(reverse('accounts:patient_dashboard'))  # Update the URL name here
    else:
        form = PatientCreationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/patient_signup.html', context)


def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Create a Doctor instance for the user
            # Redirect to the doctor dashboard or any desired page
            return redirect(reverse('accounts:doctor_dashboard'))  # Update the URL name here
    else:
        form = DoctorCreationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/doctor_signup.html', context)


@login_required
def patient_dashboard(request):
    # Get the logged-in patient
    patient = get_object_or_404(Patient, user=request.user)

    context = {
        'patient': patient
    }

    # Logic for patient dashboard view
    return render(request, 'accounts/patient_dashboard.html', context)


@login_required
def doctor_dashboard(request):
    # Get the logged-in doctor
    doctor = get_object_or_404(Doctor, user=request.user)

    context = {
        'doctor': doctor
    }

    # Logic for doctor dashboard view
    return render(request, 'accounts/doctor_dashboard.html', context)

@login_required
def profile(request):
    # Retrieve the logged-in user's profile information
    user = request.user
    # Add any additional logic here to retrieve and pass data to the template
    return render(request, 'accounts/profile.html', {'user': user})
