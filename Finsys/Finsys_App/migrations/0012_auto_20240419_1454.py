# Generated by Django 3.2.23 on 2024-04-19 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0011_alter_fin_retainer_invoice_customer_gst_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fin_retainer_invoice',
            name='Company',
        ),
        migrations.RemoveField(
            model_name='fin_retainer_invoice',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='fin_retainer_invoice',
            name='LoginDetails',
        ),
    ]
