# Generated by Django 2.2.7 on 2020-01-04 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200104_1921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ('address',), 'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
    ]