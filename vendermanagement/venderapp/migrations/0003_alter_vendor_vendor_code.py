# Generated by Django 5.0 on 2023-12-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venderapp', '0002_vendor_is_active_vendor_is_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(editable=False, max_length=255, unique=True),
        ),
    ]
