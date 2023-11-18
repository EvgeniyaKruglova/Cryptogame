# Generated by Django 4.2.7 on 2023-11-18 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_celery_beat', '0018_improve_crontab_helptext'),
        ('Cryptogameapp', '0002_taskcard_last_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskcard',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.RemoveField(
            model_name='taskcard',
            name='beginning_date',
        ),
        migrations.RemoveField(
            model_name='taskcard',
            name='description',
        ),
        migrations.RemoveField(
            model_name='taskcard',
            name='name',
        ),
        migrations.AddField(
            model_name='taskcard',
            name='card_task',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='card_task', to='django_celery_beat.periodictask'),
        ),
        migrations.AlterField(
            model_name='taskcard',
            name='last_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='taskcard',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cryptogameapp.creator'),
        ),
    ]
