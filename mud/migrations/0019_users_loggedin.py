# Generated by Django 2.2.3 on 2019-07-22 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mud', '0018_auto_20190718_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='loggedIn',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
