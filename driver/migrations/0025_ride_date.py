# Generated by Django 2.2.1 on 2019-08-11 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0024_driver_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]