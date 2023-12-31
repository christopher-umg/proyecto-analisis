# Generated by Django 3.2 on 2023-10-27 21:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='Estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='Tipo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
