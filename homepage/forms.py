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

    outcomes = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 6,
            "placeholder": "Mỗi dòng là một outcome"
        }),
        required=False
    )

    class Meta:
        model = Course
        fields = [
            "title",
            "description",
            "level",
            "duration",
            "lecturer",
            "outcomes"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields["outcomes"].initial = "\n".join(
                self.instance.outcomes
            )

    def clean_outcomes(self):
        text = self.cleaned_data["outcomes"]

        return [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]