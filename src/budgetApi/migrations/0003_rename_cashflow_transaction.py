# Generated by Django 4.0.1 on 2022-01-30 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgetApi', '0002_cashflow_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CashFlow',
            new_name='Transaction',
        ),
    ]