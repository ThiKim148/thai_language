from django.urls import path

# pyrefly: ignore [missing-import]
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("courses/", views.courses, name="courses"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path('weather/', views.weather_page, name='weather_page'),
    path('api/weather/', views.weather, name='api_weather'),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    
    # Trang admin tùy chỉnh
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/courses/", views.course_list, name="course_list"),
    path("dashboard/courses/create/", views.course_create, name="course_create"),
    path("dashboard/courses/<int:pk>/edit/", views.course_edit, name="course_edit"),
    path("dashboard/courses/<int:pk>/delete/", views.course_delete, name="course_delete"),
    path("dashboard/contacts/", views.contact_list, name="contact_list"),
]
