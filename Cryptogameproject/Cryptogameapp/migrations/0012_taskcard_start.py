# Generated by Django 4.2.7 on 2023-11-25 09:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Cryptogameapp', '0011_taskcard_definition'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcard',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]