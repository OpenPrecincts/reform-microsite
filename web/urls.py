from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView

admin.site.site_header = "PGP Reforms Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
]
