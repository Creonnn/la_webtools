from django.shortcuts import render # This is imported by default. Render basically takes in an HTML file and renders is instead of using HttpResponse
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})