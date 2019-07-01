from django.db import models
from markupfield.fields import MarkupField


class State(models.Model):
    abbreviation = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=30)

    draws_congressional_lines = models.CharField(max_length=300, blank=True)
    draws_state_lines = models.CharField(max_length=300, blank=True)
    legislative_control = models.CharField(max_length=300, blank=True)

    process = MarkupField(markup_type="markdown", blank=True)
    issues = MarkupField(markup_type="markdown", blank=True)
    actions = MarkupField(markup_type="markdown", blank=True)
    pitfalls = MarkupField(markup_type="markdown", blank=True)
    contacts = MarkupField(markup_type="markdown", blank=True)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
