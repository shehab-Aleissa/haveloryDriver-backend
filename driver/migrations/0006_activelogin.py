# Generated by Django 2.2.1 on 2019-06-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0005_ride'),
    ]

    operations = [
        migrations.CreateModel(
            name='activeLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.BigIntegerField()),
                ('active', models.BooleanField()),
                ('location', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
