from django.shortcuts import render, get_object_or_404
from .models import State


def state_page(request, abbr):
    state = get_object_or_404(State, pk=abbr.upper())

    return render(request, "state.html", {
        "state": state,
    })
