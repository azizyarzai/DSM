# Generated by Django 2.2.7 on 2019-12-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191226_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]
