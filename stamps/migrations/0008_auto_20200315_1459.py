# Generated by Django 2.2.7 on 2020-03-15 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stamps', '0007_group_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='discount',
        ),
        migrations.AddField(
            model_name='category',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
