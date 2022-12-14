# Generated by Django 4.0.4 on 2022-12-27 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0017_waiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('apply', '지원'), ('judge', '심사'), ('act', '활동'), ('etc', '기타')], max_length=10)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
