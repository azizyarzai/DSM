# Generated by Django 2.2.7 on 2020-01-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_charges',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]