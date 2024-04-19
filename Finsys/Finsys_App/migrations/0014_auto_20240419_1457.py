# Generated by Django 3.2.23 on 2024-04-19 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0013_auto_20240419_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='fin_retainer_invoice',
            name='Company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details'),
        ),
        migrations.AddField(
            model_name='fin_retainer_invoice',
            name='Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_customers'),
        ),
        migrations.AddField(
            model_name='fin_retainer_invoice',
            name='LoginDetails',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details'),
        ),
        migrations.AddField(
            model_name='fin_retainer_invoice_comments',
            name='Ret_Invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_retainer_invoice'),
        ),
        migrations.AddField(
            model_name='fin_retainer_invoice_history',
            name='Ret_Invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_retainer_invoice'),
        ),
        migrations.AddField(
            model_name='fin_retainer_invoice_items',
            name='Ret_Inv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_retainer_invoice'),
        ),
    ]
