from django.urls import path

# pyrefly: ignore [missing-import]
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("courses/", views.courses, name="courses"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('weather/', views.weather_page, name='weather_page'),
    path('api/weather/', views.weather, name='api_weather'),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
]
