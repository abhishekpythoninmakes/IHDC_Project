# Generated by Django 5.0.3 on 2024-06-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_alter_transaction_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
