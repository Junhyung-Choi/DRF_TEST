# Generated by Django 4.0.4 on 2022-12-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_alter_application_generation_alter_application_major_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='myAttribute',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
