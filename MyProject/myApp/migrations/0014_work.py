# Generated by Django 4.0.4 on 2022-12-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_alter_about_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='Work/%Y/%m/%d')),
            ],
        ),
    ]