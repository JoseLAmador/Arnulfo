# Generated by Django 2.0.1 on 2018-05-09 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0014_auto_20180508_0559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleitem',
            name='animal_ref',
        ),
        migrations.RemoveField(
            model_name='saleitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='saleitem',
            name='unit_price',
        ),
        migrations.RemoveField(
            model_name='saleitem',
            name='weigth',
        ),
    ]
