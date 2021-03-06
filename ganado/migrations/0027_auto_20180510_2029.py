# Generated by Django 2.0.1 on 2018-05-10 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganado', '0026_auto_20180417_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.RemoveField(
            model_name='animal',
            name='ref_factura_original',
        ),
        migrations.AddField(
            model_name='animal',
            name='ref_factura_original',
            field=models.ManyToManyField(related_name='animals', to='ganado.Factura'),
        ),
    ]
