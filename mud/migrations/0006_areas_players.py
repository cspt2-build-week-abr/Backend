# Generated by Django 2.2.3 on 2019-07-12 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mud', '0005_auto_20190710_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='areas',
            name='players',
            field=models.TextField(blank=True),
        ),
    ]