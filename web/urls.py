from django.contrib import admin
from django.urls import path
from django.conf import settings
from reforms import views, feed

admin.site.site_header = "PGP Reforms Admin"

urlpatterns = [
    path(settings.PREFIX + "feed/", feed.StateFeed()),
    path(settings.PREFIX + "admin/", admin.site.urls),
    path(settings.PREFIX + "us-states/", views.us_json),
    path(settings.PREFIX + "", views.index),
    path(settings.PREFIX + "export-book/", views.export),
    path(settings.PREFIX + "basic/", views.basic_view),
    path(settings.PREFIX + "<str:abbr>/", views.state_page),
]
