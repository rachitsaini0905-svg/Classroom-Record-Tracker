
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student


def home(request):
    return render(request, 'school website.html')

# def login_view(request):
#     return render(request,'login.html')


# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account created successfully!')
#             return redirect('login')

#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})




# from django.shortcuts import render, redirect
# from .models import Student

# def student_table(request):
#     print("🎯 student_table view is working!")  # See this in terminal
#     students = Student.objects.all()
#     # return HttpResponse("✅ View is working")
    
#     return render(request, 'student_table.html', {'students': students})

from django.shortcuts import render
from .models import Student, SubjectMark
from collections import defaultdict

def student_table(request):
    students = Student.objects.all().prefetch_related('subjectmark_set')

    grouped_students = defaultdict(list)

    for student in students:
        # Convert subject marks into a dictionary
        marks_dict = {mark.subject.lower(): mark.marks for mark in student.subjectmark_set.all()}

        # Attach dynamic subject marks to the student for template access
        student.subject_marks = marks_dict
        grouped_students[student.class_name].append(student)

    return render(request, 'student_table.html', {'grouped_students': dict(grouped_students)})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.roll_number = request.POST['roll_number']
        student.class_name = request.POST['class_name']
        student.maths_marks = request.POST['maths_marks']
        student.science_marks = request.POST['science_marks']
        student.english_marks = request.POST['english_marks']
        student.save()
    
    return redirect('students')  # just go back to the student table after saving


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('students')