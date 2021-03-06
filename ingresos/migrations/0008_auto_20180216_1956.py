# Generated by Django 2.0.1 on 2018-02-16 19:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0007_auto_20180214_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='contact_check',
            new_name='direct_contact',
        ),
        migrations.RemoveField(
            model_name='client',
            name='contact',
        ),
        migrations.AddField(
            model_name='client',
            name='comments_contact',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name='client',
            name='name_contact',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name='client',
            name='phone_contact',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.", regex='^\\+?1?\\d{9,10}$')]),
        ),
    ]
