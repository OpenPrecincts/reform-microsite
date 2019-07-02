from django.contrib import admin
from django.urls import path
from reforms import views

admin.site.site_header = "PGP Reforms Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("us-states/", views.us_json),
    path("", views.index),
    path("export-book/", views.export),
    path("<str:abbr>/", views.state_page),
]
