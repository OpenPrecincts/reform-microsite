from django.contrib import admin
from .models import State, Comment


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    readonly_fields = ("name", "abbreviation")
    ordering = ("name",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "from_email", "state", "created")
    readonly_fields = ("comment", "name", "from_email", "state")
    list_filter = ("state",)
    ordering = ("created",)
