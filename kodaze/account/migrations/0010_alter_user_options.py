# Generated by Django 3.2.12 on 2022-08-30 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'default_permissions': (), 'ordering': ('pk',), 'permissions': ()},
        ),
    ]
