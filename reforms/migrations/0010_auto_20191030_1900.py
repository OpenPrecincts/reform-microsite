# Generated by Django 2.2.5 on 2019-10-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reforms', '0009_state_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='map_drawing_links',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='state',
            name='op_link',
            field=models.URLField(blank=True),
        ),
    ]
