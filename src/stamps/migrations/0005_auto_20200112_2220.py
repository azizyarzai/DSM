# Generated by Django 2.2.7 on 2020-01-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stamps', '0004_auto_20200104_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, unique=True),
        ),
    ]
