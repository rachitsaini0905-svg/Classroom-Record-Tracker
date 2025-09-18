from django import template

register = template.Library()

@register.filter
def get_subject(marks, subject_name):
    return marks.filter(subject_name=subject_name).first()
