# Generated by Django 2.2.7 on 2020-03-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stamps', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='Type',
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ('name',), 'verbose_name': 'Type', 'verbose_name_plural': 'Types'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='group',
            new_name='stamp_type',
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterModelTable(
            name='type',
            table='type',
        ),
    ]
