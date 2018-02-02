# Generated by Django 2.0.1 on 2018-01-30 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='payment',
            field=models.CharField(choices=[('Tarjeta Credito', 'Tarjeta Credito'), ('Efectivo', 'Efectivo'), ('Tarjeta Debito', 'Tarjeta Debito')], max_length=100),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='egresos.Provider'),
        ),
    ]