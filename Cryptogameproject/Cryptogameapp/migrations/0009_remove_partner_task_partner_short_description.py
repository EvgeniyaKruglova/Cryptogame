# Generated by Django 4.2.7 on 2023-11-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cryptogameapp', '0008_remove_award_description_award_experience_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='task',
        ),
        migrations.AddField(
            model_name='partner',
            name='short_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
