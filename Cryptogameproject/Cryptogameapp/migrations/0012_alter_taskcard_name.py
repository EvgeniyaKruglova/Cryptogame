# Generated by Django 4.2.7 on 2023-11-23 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0018_improve_crontab_helptext'),
        ('Cryptogameapp', '0011_remove_taskcard_start_date_alter_taskcard_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcard',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='django_celery_beat.periodictask', to_field='name'),
        ),
    ]