from django.db import models
from django.core.validators import RegexValidator
from ingresos.models import BusinessLine

class Provider(models.Model):
    provider = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    rfc = models.CharField(max_length=20, default="", unique=True)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    direct_contact = models.BooleanField(default=False)
    name_contact = models.CharField(max_length=140, blank=True)
    phone_contact = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    comments_contact = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return self.provider

    class Meta:
        ordering = ["-id"]

class Compras(models.Model):
    no_factura = models.CharField(max_length=140)
    descripcion = models.CharField(max_length=140)
    fecha_creacion = models.DateField(auto_now_add=False, db_index=True, blank=True, null=True)
    costo_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    linea_compras = models.ForeignKey(BusinessLine, related_name="compras", on_delete=models.PROTECT, blank=True,
                                      null=True)
    proveedor = models.ForeignKey(Provider, related_name="compras", on_delete=models.PROTECT, blank=True, null=True)


    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.no_factura



class Purchase (models.Model):
    LINES = (('Cerdos', 'Cerdos'),
                ('Ganado', 'Ganado'),
                ('Granos', 'Granos'),
                ('Planta de alimentos','Planta de alimentos'),
                ('Campo', 'Campo')
             )
    TYPE = (('Gasto', 'Gasto'),
             ('Costo', 'Costo'),
             )
    created = models.DateTimeField(auto_now_add=True)
    provider_egreso = models.ForeignKey(Provider, related_name="purchases", on_delete=models.PROTECT, blank=True, null=True)
    purchase_check = models.BooleanField(default=False)
    no_check = models.CharField(max_length=140, blank=True, null=True)
    paid = models.BooleanField(default=False)
    business_egreso = models.ForeignKey(BusinessLine, related_name="purchases", on_delete=models.PROTECT, blank=True,
                                      null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type = models.CharField(max_length=100, choices=TYPE, blank=True, null=True)
    concepto_purchase = models.CharField(max_length=140, blank=True, null=True)
    compra_egreso = models.ForeignKey(Compras, related_name="purchases", on_delete=models.PROTECT, blank=True,
                                      null=True)
    compra_check = models.BooleanField(default=False)


    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return "Compra no. {}".format(self.id)


class Product(models.Model):
    name = models.CharField(max_length= 140)
    category = models.CharField(max_length = 140)
    uprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class GastoGanado(models.Model):
    concepto = models.CharField(max_length = 140)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True, db_index=True, blank=True, null=True)


#Prueba

class PurchaseItem(models.Model):
    order = models.ForeignKey(Purchase, related_name='items', on_delete=models.PROTECT)
    #product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weigth = models.DecimalField(max_digits=10, decimal_places=2)
    animal_ref = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.product.uprice*self.weigth

