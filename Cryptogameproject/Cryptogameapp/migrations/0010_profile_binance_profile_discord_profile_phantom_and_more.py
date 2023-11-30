# Generated by Django 4.2.7 on 2023-11-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cryptogameapp', '0009_remove_partner_task_partner_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Binance',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Discord',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Phantom',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Telegram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='TrustWallet',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='metaMask',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taskcard',
            name='published',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='taskcard',
            name='title',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
