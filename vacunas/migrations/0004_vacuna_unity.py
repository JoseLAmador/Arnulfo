# Generated by Django 2.0.1 on 2018-03-08 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacunas', '0003_auto_20180308_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacuna',
            name='unity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
