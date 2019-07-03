import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .models import State, CommentForm


def us_json(request):
    return render(request, "us-states.json", {})


def index(request):
    state_data = list(State.objects.values("name", "legislative_control", "actions"))
    for s in state_data:
        action = re.split(r"\.\s", s["actions"])[0]
        s["short_action"] = action + "." if action else ""
    return render(request, "index.html", {"state_data": state_data})


def state_page(request, abbr):
    if len(abbr) > 2:
        state = get_object_or_404(State, name__iexact=abbr)
        return redirect("/" + settings.PREFIX + f"{state.abbreviation.lower()}/")
    if not abbr.islower():
        return redirect("/" + settings.PREFIX + f"{abbr.lower()}/")
    state = get_object_or_404(State, pk=abbr.upper())
    reveal_form = False

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            form = CommentForm(initial={"state": abbr.upper()})
            messages.success(
                request, "Comment submitted!  Thank you for your feedback!"
            )
        else:
            messages.error(
                request, "Please review the errors & re-submit your comment."
            )
            reveal_form = True
    else:
        form = CommentForm(initial={"state": abbr.upper()})

    return render(
        request,
        "state.html",
        {"state": state, "comment_form": form, "reveal_form": reveal_form},
    )


def export(request):
    states = list(State.objects.all().order_by("name"))
    resp = render(request, "export.html", {"states": states}, content_type="text/xml")
    resp["Content-Disposition"] = 'attachment; filename="export.xml"'
    return resp
