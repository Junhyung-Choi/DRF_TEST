# Generated by Django 4.0.4 on 2022-12-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_customuser_myattribute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='myAttribute',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
