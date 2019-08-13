from django.core.management.base import BaseCommand
from ...models import State
import yaml


class Command(BaseCommand):
    help = "Export data to YAML"

    def handle(self, *args, **options):
        for state in State.objects.values():
            with open(f'data/{state["abbreviation"]}.yml', "w") as f:
                for k in list(state.keys()):
                    if k.startswith("_"):
                        state.pop(k)
                yaml.dump(state, f)
