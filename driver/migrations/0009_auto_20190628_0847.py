# Generated by Django 2.2.1 on 2019-06-28 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0008_auto_20190628_0800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activelogin',
            old_name='user_Id',
            new_name='username',
        ),
    ]