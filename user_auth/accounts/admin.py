from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Patient, Doctor

User = get_user_model()

admin.site.register(Patient)
admin.site.register(Doctor)
