from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import State, CommentForm


def state_page(request, abbr):
    if not abbr.islower():
        return redirect(f"/{abbr.lower()}/")
    state = get_object_or_404(State, pk=abbr.upper())
    reveal_form = False

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            form = CommentForm(initial={"state": abbr.upper()})
            messages.success(request, "Comment submitted!  Thank you for your feedback!")
        else:
            messages.error(request, "Please review the errors & re-submit your comment.")
            reveal_form = True
    else:
        form = CommentForm(initial={"state": abbr.upper()})

    return render(request, "state.html", {
        "state": state,
        "comment_form": form,
        "reveal_form": reveal_form,
    })
