# Generated by Django 2.0.1 on 2018-03-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganado', '0024_auto_20180326_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='arete_siniga',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
