# Generated by Django 2.2.7 on 2020-01-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='active',
        ),
        migrations.AddField(
            model_name='cart',
            name='checked_out',
            field=models.BooleanField(default=True),
        ),
    ]
