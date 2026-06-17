from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Course, Contact

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ["username", "email", "phone", "password1", "password2"]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "level", "duration", "lecturer"]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]