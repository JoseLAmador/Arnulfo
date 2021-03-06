# Generated by Django 2.0.1 on 2018-02-27 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ganado', '0015_animal_merma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='animal',
            name='raza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='ganado.Raza'),
        ),
    ]
