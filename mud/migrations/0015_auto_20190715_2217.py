# Generated by Django 2.2.3 on 2019-07-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mud', '0014_areas_exits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areas',
            name='adjacents',
        ),
        migrations.AddField(
            model_name='areas',
            name='coords',
            field=models.TextField(blank=True, null=True),
        ),
    ]