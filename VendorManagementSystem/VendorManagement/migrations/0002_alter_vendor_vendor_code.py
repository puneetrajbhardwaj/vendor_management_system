# Generated by Django 4.0.1 on 2024-05-04 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VendorManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]