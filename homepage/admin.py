from django.contrib import admin

from homepage.models import Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "lecturer", "duration", "level")