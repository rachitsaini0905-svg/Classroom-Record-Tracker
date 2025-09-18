# In your urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.teacher_login, name='login'),
    # Add your other views here
    path('home/', views.teacher_home, name='teacher_home'),
]
