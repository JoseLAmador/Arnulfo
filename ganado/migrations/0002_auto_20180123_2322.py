# Generated by Django 2.0.1 on 2018-01-23 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ganado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastoanimal',
            name='animal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aliments', to='ganado.Animal'),
        ),
    ]
