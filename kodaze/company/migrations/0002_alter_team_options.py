# Generated by Django 3.2.12 on 2022-08-27 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'default_permissions': [], 'ordering': ('pk',), 'permissions': (('view_team', 'Mövcud komandalara baxa bilər'), ('add_team', 'Komanda əlavə edə bilər'), ('change_team', 'Komanda məlumatlarını yeniləyə bilər'), ('delete_team', 'Komanda silə bilər'))},
        ),
    ]