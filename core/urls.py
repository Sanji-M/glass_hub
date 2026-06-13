#Parent core/urls.py

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

# The `urlpatterns` list routes URLs to views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('hub.urls')),
]


# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


