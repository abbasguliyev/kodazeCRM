# Generated by Django 3.2.12 on 2022-08-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup_restore', '0002_auto_20220827_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='backupandrestore',
            name='backup_type',
            field=models.CharField(blank=True, choices=[('backup', 'backup'), ('media_backup', 'media_backup'), ('restore', 'restore')], default=None, max_length=150, null=True),
        ),
    ]
