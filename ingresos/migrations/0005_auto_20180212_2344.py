# Generated by Django 2.0.1 on 2018-02-12 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0004_sale_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='contact',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='contact_check',
            field=models.BooleanField(default=False),
        ),
    ]
