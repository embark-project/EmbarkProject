# Generated by Django 3.2.8 on 2022-01-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20220112_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='order',
            name='approved_status',
            field=models.IntegerField(default=0),
        ),
    ]
