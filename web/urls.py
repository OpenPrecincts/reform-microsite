from django.contrib import admin
from django.urls import path
from reforms import views

admin.site.site_header = "PGP Reforms Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("<str:abbr>/", views.state_page),
]
