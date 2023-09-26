from django.contrib import admin
from django.urls import path
from mmappp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
]
