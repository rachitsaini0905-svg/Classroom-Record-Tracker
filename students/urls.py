from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #  path('login/', views.login_view, name='login'),
    # path('signup/', views.signup_view, name='signup'),
   
    path('students/', views.student_table, name='students'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student')
    
    # path('students/', views.student_table, name='students'),

]
