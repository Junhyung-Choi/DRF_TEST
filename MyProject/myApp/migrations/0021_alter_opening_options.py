# Generated by Django 4.0.4 on 2022-12-27 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0020_opening_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opening',
            options={'get_latest_by': 'id'},
        ),
    ]
