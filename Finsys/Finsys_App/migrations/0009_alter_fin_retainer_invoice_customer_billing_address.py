# Generated by Django 3.2.23 on 2024-04-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0008_fin_retainer_invoice_items_sac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fin_retainer_invoice',
            name='Customer_billing_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
