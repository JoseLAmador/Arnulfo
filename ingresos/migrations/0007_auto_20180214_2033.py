# Generated by Django 2.0.1 on 2018-02-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0006_client_rfc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='contact_check',
        ),
        migrations.AddField(
            model_name='client',
            name='contact',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='contact_check',
            field=models.BooleanField(default=False),
        ),
    ]
