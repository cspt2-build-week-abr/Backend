# Generated by Django 2.2.3 on 2019-07-19 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mud', '0017_auto_20190716_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='area_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
