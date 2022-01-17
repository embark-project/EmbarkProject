# Generated by Django 3.2.8 on 2022-01-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_remove_order_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reason',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_type',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
