# Generated by Django 2.2.3 on 2019-07-12 02:44

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('mud', '0007_auto_20190711_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokeballs',
            name='catchRate',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='pokeballs',
            name='spawnChance',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='catchChance',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='spawnChance',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True),
        ),
    ]
