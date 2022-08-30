# Generated by Django 3.2.12 on 2022-08-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
    ]
