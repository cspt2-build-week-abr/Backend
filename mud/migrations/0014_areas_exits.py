# Generated by Django 2.2.3 on 2019-07-16 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mud', '0013_auto_20190715_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='areas',
            name='exits',
            field=models.TextField(blank=True, null=True),
        ),
    ]
