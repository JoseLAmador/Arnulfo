# Generated by Django 2.0.1 on 2018-02-27 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacunas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacuna',
            name='concentration',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='content',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='dose',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
