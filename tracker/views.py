from django.conf import settings
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime

@api_view(["GET"])
def bus_location(request):
    # Simulated bus location (changes every minute)
    now = datetime.datetime.now().minute
    lat = 10.048 + (now % 10) * 0.001
    lng = 76.327 + (now % 10) * 0.001
    return Response({"lat": lat, "lng": lng})

# 👇 Add this function for the map page
def show_map(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY or ""
    }
    return render(request, "map.html", context)

def bus_tracker(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'bus_tracker.html', context)
