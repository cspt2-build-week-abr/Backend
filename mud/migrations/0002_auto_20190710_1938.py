# Generated by Django 2.2.3 on 2019-07-11 02:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('pokemon', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
