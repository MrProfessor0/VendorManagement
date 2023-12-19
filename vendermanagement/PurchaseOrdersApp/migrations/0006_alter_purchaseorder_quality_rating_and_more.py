# Generated by Django 5.0 on 2023-12-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseOrdersApp', '0005_purchaseorder_id_alter_purchaseorder_po_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='quality_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending', max_length=255),
        ),
    ]
