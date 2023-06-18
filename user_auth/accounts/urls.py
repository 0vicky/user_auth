from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('patient_signup/', views.patient_signup, name='patient_signup'),
    path('doctor_signup/', views.doctor_signup, name='doctor_signup'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('profile/', views.profile, name='profile'),

]
