# Generated by Django 3.2.12 on 2022-08-27 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbox', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='officecashbox',
            options={'default_permissions': [], 'ordering': ('pk',), 'permissions': (('view_officecashbox', 'Mövcud ofis kassalara baxa bilər'), ('add_officecashbox', 'Ofis kassa əlavə edə bilər'), ('change_officecashbox', 'Ofis kassa məlumatlarını yeniləyə bilər'), ('delete_officecashbox', 'Ofis kassa silə bilər'))},
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='company_initial_balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='company_subsequent_balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='holding_initial_balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='holding_subsequent_balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='initial_balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='office_initial_balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='office_subsequent_balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='subsequent_balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='companycashbox',
            name='balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='holdingcashbox',
            name='balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='officecashbox',
            name='balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
    ]