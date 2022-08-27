# Generated by Django 3.2.12 on 2022-08-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbox', '0003_auto_20220827_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='company_initial_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='company_subsequent_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='holding_initial_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='holding_subsequent_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='initial_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='office_initial_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='office_subsequent_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='subsequent_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='companycashbox',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='holdingcashbox',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='officecashbox',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]