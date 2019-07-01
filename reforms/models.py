from django.db import models
from markupfield.fields import MarkupField


class StateInformation(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=2)

    draws_congressional_lines = models.CharField(max_length=300)
    draws_state_lines = models.CharField(max_length=300)
    legislative_control = models.CharField(max_length=300)

    process = MarkupField(markup_type="markdown")
    issues = MarkupField(markup_type="markdown")
    actions = MarkupField(markup_type="markdown")
    pitfalls = MarkupField(markup_type="markdown")
    contacts = MarkupField(markup_type="markdown")

    last_updated = models.DateTimeField(auto_now=True)
