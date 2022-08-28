# Generated by Django 3.2.12 on 2022-08-28 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_auto_20220827_1553'),
        ('account', '0007_rename_manager_user_supervisor'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='account.customer'),
        ),
        migrations.AlterField(
            model_name='service',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='contract.contract'),
        ),
    ]
