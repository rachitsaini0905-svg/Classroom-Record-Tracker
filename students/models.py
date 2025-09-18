# models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    class_name = models.CharField(max_length=20)

    def get_total(self):
        return sum(mark.marks for mark in self.subjectmark_set.all())

    def get_percentage(self):
        total_subjects = self.subjectmark_set.count()
        return round(self.get_total() / total_subjects, 2) if total_subjects else 0

    def get_status(self):
        return "Passed" if self.get_percentage() >= 40 else "Failed"

    def __str__(self):
        return f"{self.roll_number} - {self.name}"


class SubjectMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.marks}"
