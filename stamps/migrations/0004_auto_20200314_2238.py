# Generated by Django 2.2.7 on 2020-03-14 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stamps', '0003_product_diameter'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='Group',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stamp_type',
            new_name='group',
        ),
    ]
