# Generated by Django 3.2.12 on 2022-08-27 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customer_order_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=12),
        ),
    ]
