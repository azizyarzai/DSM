# Generated by Django 2.2.7 on 2020-01-12 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stamps', '0007_auto_20200113_0040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('name',), 'verbose_name': 'group', 'verbose_name_plural': 'groups'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
