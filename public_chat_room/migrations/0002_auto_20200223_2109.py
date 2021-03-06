# Generated by Django 3.0.3 on 2020-02-23 21:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('public_chat_room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
