# Generated by Django 2.0.1 on 2018-05-08 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0011_auto_20180504_2240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['-id']},
        ),
    ]
