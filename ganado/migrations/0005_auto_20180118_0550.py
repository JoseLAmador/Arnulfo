# Generated by Django 2.0.1 on 2018-01-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganado', '0004_auto_20180116_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corral',
            name='fecha_generacion',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]