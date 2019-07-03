from django.db import migrations
import us


def forwards(apps, schema_editor):
    State = apps.get_model("reforms", "State")

    for state in us.states.STATES:
        State.objects.create(name=state.name, abbreviation=state.abbr)


class Migration(migrations.Migration):

    dependencies = [("reforms", "0001_initial")]

    operations = [migrations.RunPython(forwards)]
