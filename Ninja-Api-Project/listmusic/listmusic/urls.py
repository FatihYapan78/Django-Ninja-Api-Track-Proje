from django.contrib import admin
from django.urls import path
from track.views import *
from track.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("", index, name="index")
]
