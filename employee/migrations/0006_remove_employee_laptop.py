# Generated by Django 3.1.5 on 2021-01-26 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20210126_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='laptop',
        ),
    ]
