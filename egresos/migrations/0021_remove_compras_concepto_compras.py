# Generated by Django 2.0.1 on 2018-05-23 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0020_auto_20180523_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras',
            name='concepto_compras',
        ),
    ]
