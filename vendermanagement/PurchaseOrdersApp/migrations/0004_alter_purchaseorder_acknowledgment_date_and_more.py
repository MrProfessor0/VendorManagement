# Generated by Django 5.0 on 2023-12-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseOrdersApp', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='acknowledgment_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='quality_rating',
            field=models.FloatField(default=None, null=True),
        ),
    ]
