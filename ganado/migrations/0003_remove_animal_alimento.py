# Generated by Django 2.0.1 on 2018-01-08 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ganado', '0002_auto_20180108_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='alimento',
        ),
    ]
