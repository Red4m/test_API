# Generated by Django 3.1.5 on 2021-01-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0002_auto_20210126_1907'),
        ('employee', '0003_auto_20210126_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='laptop',
            field=models.ManyToManyField(blank=True, default=None, to='laptops.Laptops'),
        ),
    ]
