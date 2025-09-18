from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# 📘 This is the helper (manager) that creates teacher users
class TeacherAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required to create a teacher")
        email = self.normalize_email(email)  # cleans the email (removes spaces etc.)
        teacher = self.model(email=email, **extra_fields)
        teacher.set_password(password)       # saves the password safely (hashed)
        teacher.save(using=self._db)         # save to the database
        return teacher

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)       # can access admin panel
        extra_fields.setdefault('is_superuser', True)   # has all permissions
        return self.create_user(email, password, **extra_fields)


# 👨‍🏫 This is the main Teacher model (used for login)
class Teacher(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)              # login using email
    full_name = models.CharField(max_length=100)        # teacher's name
    subject_specialization = models.CharField(max_length=100)  # subject they teach
    contact_number = models.CharField(max_length=15, blank=True)  # optional phone

    is_active = models.BooleanField(default=True)       # can log in
    is_staff = models.BooleanField(default=False)       # can access admin dashboard

    objects = TeacherAccountManager()                   # use the custom manager above

    USERNAME_FIELD = 'email'                            # login with email instead of username
    REQUIRED_FIELDS = ['full_name']                     # required when creating superuser

    def __str__(self):
        return self.full_name or self.email             # display name in admin panel

