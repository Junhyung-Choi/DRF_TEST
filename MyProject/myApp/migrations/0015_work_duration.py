# Generated by Django 4.0.4 on 2022-12-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0014_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='duration',
            field=models.CharField(choices=[('1', '1학기'), ('1.5', '여름방학'), ('2', '2학기')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
