# Generated by Django 2.0.1 on 2018-05-10 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0014_auto_20180509_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='business_line',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
