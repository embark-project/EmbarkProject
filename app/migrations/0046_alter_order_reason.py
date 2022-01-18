# Generated by Django 3.2.8 on 2022-01-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_alter_order_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='reason',
            field=models.CharField(choices=[('approved', 'Approved: Your requested has been approved'), ('rejected1', 'Rejected: Out of stock'), ('rejected2', 'Rejected: Unavailabilty of sufficient quantity'), ('rejected3', 'Rejected: reason 3')], max_length=120),
        ),
    ]
