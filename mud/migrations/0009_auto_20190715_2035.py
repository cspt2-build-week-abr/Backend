# Generated by Django 2.2.3 on 2019-07-16 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mud', '0008_auto_20190711_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
