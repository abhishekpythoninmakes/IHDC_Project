# Generated by Django 5.0.3 on 2024-06-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=30)),
                ('account_number', models.BigIntegerField()),
                ('ifsc_code', models.CharField(max_length=14)),
            ],
        ),
    ]