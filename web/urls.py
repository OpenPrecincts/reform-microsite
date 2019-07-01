from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView
from reforms import views

admin.site.site_header = "PGP Reforms Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("<str:abbr>/", views.state_page),
]
