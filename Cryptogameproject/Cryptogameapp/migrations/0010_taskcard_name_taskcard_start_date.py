# Generated by Django 4.2.7 on 2023-11-23 18:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0018_improve_crontab_helptext'),
        ('Cryptogameapp', '0009_remove_partner_task_partner_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcard',
            name='name',
            field=models.OneToOneField(default='None', on_delete=django.db.models.deletion.PROTECT, to='django_celery_beat.periodictask', to_field='name'),
        ),
        migrations.AddField(
            model_name='taskcard',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
