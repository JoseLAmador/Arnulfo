# Generated by Django 2.0.1 on 2018-05-23 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0021_auto_20180522_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleitem',
            name='product',
        ),
    ]