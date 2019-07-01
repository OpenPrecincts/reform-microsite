from django.contrib import admin
from .models import State

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    readonly_fields = ("name", "abbreviation")
    ordering = ("name",)
