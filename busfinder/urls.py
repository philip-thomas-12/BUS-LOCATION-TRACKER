from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from tracker.views import bus_location, show_map

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bus/", bus_location),
    path("map/", show_map),
    path("", lambda request: HttpResponseRedirect("/map/")),  # 👈 default root -> map
]
