# Generated by Django 3.2.12 on 2022-08-28 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20220828_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='receiving_warehouse',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='receiving_warehouse', to='warehouse.warehouse'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operation',
            name='shipping_warehouse',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_warehouse', to='warehouse.warehouse'),
            preserve_default=False,
        ),
    ]
