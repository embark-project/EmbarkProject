# Generated by Django 3.2.8 on 2022-01-08 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20220108_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_type',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user_type',
            name='is_enduser',
        ),
        migrations.RemoveField(
            model_name='user_type',
            name='is_moderator',
        ),
    ]
