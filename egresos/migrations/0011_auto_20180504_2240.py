# Generated by Django 2.0.1 on 2018-05-04 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0010_auto_20180222_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provider',
            options={'ordering': ['-id']},
        ),
    ]