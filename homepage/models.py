from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# User tuỳ chỉnh kế thừa từ AbstractUser
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    lecturer = models.CharField(max_length=100)
    outcomes = models.JSONField(default=list)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "course"],
                name="unique_user_course"
            )
        ]

    def __str__(self):
        return f"{self.user.username} đăng ký {self.course.title}"

class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Liên hệ từ {self.name} - {self.email}"