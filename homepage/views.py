from django.http import Http404
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
import requests

from homepage.models import Contact, Course, Enrollment
from .mock_data import COURSES
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CourseForm


def index(request):
    return render(request, "homepage/index.html", {"courses": COURSES})

def courses(request):
    return render(request, "homepage/courses.html", {"courses": COURSES})

def about(request):
    return render(request, "homepage/about.html")

def contact_view(request):
    if request.method == "POST":
        message = request.POST.get("message")
        if request.user.is_authenticated:
            Contact.objects.create(
                user=request.user,
                name=request.user.get_full_name() or request.user.username,
                email=request.user.email,
                message=message
            )
        else:
            name = request.POST.get("name")
            email = request.POST.get("email")
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
        return JsonResponse({"success": True})
    return render(request, "homepage/contact.html")

def course_detail(request, course_id):
    course = next((c for c in COURSES if c["id"] == course_id), None)
    if not course:
        raise Http404("Course not found")
    return render(request, "homepage/course_detail.html", {"course": course})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "homepage/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "homepage/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")


# API weather
OPENWEATHER_API_KEY = settings.OPENWEATHER_API_KEY

def weather(request):
    city = request.GET.get("city", "Hanoi")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=vi"
    try:
        resp = requests.get(url, timeout=5)
        data = resp.json()
        if resp.status_code == 200:
            weather = {
                "city": f"{data['name']}, {data['sys']['country']}",
                "temperature": data['main']['temp'],
                "humidity": data['main']['humidity'],
                "pressure": data['main']['pressure'],
                "description": data['weather'][0]['description'].title(),
                "icon": data['weather'][0]['icon'],
            }
            return JsonResponse(weather)
        else:
            return JsonResponse({"error": data.get("message", "Không lấy được dữ liệu")}, status=400)
    except requests.RequestException:
        return JsonResponse({"error": "Lỗi kết nối API"}, status=500)

def weather_page(request):
    return render(request, "homepage/weather.html")


@staff_member_required
def admin_dashboard(request):
    courses = Course.objects.all()
    enrollments_per_course = [
        {"title": c.title, "count": c.enrollment_set.count()} for c in courses
    ]
    stats = {
        "total_courses": courses.count(),
        "total_enrollments": Enrollment.objects.count(),
        "latest_feedback": Contact.objects.order_by("-created_at")[:5],
        "enrollments_per_course": enrollments_per_course,
    }
    return render(request, "homepage/admin/dashboard.html", {"stats": stats})

@staff_member_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, "homepage/admin/course_list.html", {"courses": courses})

@staff_member_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "homepage/admin/course_form.html", {"form": form})

@staff_member_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm(instance=course)
    return render(request, "homepage/admin/course_form.html", {"form": form})

@staff_member_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect("course_list")

@staff_member_required
def contact_list(request):
    contacts = Contact.objects.order_by("-created_at")
    return render(request, "homepage/admin/contact_list.html", {"contacts": contacts})