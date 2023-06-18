from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Patient, Doctor

User = get_user_model()


class UserSelectionForm(forms.Form):
    user_type = forms.ChoiceField(
        choices=[('patient', 'Patient'), ('doctor', 'Doctor')],
        widget=forms.RadioSelect,
        required=True,
        label="I am a"
    )


class PatientCreationForm(UserCreationForm):
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
    pincode = forms.CharField(max_length=10)
    profile_picture = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        patient = Patient.objects.create(
            user=user,
            address_line1=self.cleaned_data['address_line1'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            pincode=self.cleaned_data['pincode'],
            profile_picture=self.cleaned_data['profile_picture']
        )

        return user


class DoctorCreationForm(UserCreationForm):
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
    pincode = forms.CharField(max_length=10)
    profile_picture = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        doctor = Doctor.objects.create(
            user=user,
            address_line1=self.cleaned_data['address_line1'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            pincode=self.cleaned_data['pincode'],
            profile_picture=self.cleaned_data['profile_picture'],
        )

        return user
