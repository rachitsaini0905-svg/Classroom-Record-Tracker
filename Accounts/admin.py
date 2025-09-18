from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Teacher

# 👨‍🏫 Custom admin panel for Teacher model
class TeacherAdmin(UserAdmin):
    model = Teacher

    list_display = ('email', 'full_name', 'subject_specialization', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'subject_specialization')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'subject_specialization', 'contact_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'subject_specialization', 'contact_number', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )

    search_fields = ('email', 'full_name')
    ordering = ('email',)

# ✅ Register the model and its admin panel
admin.site.register(Teacher, TeacherAdmin)
