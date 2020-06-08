# Generated by Django 2.2.7 on 2020-06-07 19:43

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stamps', '0012_auto_20200607_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='customization_descriptions',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('line1', 'Line 1'), ('line2', 'Line 2'), ('line3', 'Line 3'), ('line4', 'Line 4'), ('line5', 'Line 5'), ('text', 'Text'), ('top_outer_circle_text', 'Top Outer Circle Text'), ('monogram_initial', 'Monogram Initial'), ('center_text', 'Center Text'), ('bottom_outer_circle_text', 'Bottom Outer Circle Text'), ('below_arrow', 'Below Arrow')], max_length=999, null=True),
        ),
    ]
