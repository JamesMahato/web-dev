# Generated by Django 4.0.6 on 2022-07-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
