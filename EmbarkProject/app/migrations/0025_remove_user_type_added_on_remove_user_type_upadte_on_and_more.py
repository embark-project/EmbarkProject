# Generated by Django 4.0.1 on 2022-01-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_user_type_added_on_user_type_age_user_type_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_type',
            name='added_on',
        ),
        migrations.RemoveField(
            model_name='user_type',
            name='upadte_on',
        ),
        migrations.AlterField(
            model_name='user_type',
            name='gender',
            field=models.CharField(blank=True, default='Male', max_length=250),
        ),
    ]
