from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
import requests
from .mock_data import COURSES


def index(request):
    return render(request, "homepage/index.html", {"courses": COURSES})

def courses(request):
    return render(request, "homepage/courses.html", {"courses": COURSES})

def about(request):
    return render(request, "homepage/about.html")

def contact(request):
    return render(request, "homepage/contact.html")

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
