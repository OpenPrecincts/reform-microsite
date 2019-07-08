# Generated by Django 2.2.3 on 2019-07-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("reforms", "0008_state_gov_control")]

    operations = [
        migrations.AddField(
            model_name="state",
            name="status",
            field=models.PositiveIntegerField(
                choices=[
                    (0, "Legislative action/public input"),
                    (1, "Independent commission"),
                    (2, "Other advisory/commission"),
                    (3, "Potential reform by 2021"),
                    (4, "Divided or potentially divided gov't."),
                    (5, "Legal and legislative routes to reform"),
                ],
                default=0,
            ),
        )
    ]
