from django.db import models
from django.core.exceptions import ValidationError

class Producto(models.Model):
    codigo_prod = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    class Meta:
        app_label = 'ventas'  # Estableces el app_label aquí
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.cedula

class Venta(models.Model):
    cod_venta = models.CharField(max_length=4, primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError('La cantidad debe ser mayor que 0.')
        if self.producto.stock < self.cantidad:
            raise ValidationError('No hay stock suficiente para realizar la venta.')

    def save(self, *args, **kwargs):
        self.clean()
        self.total = self.cantidad * self.producto.precio
        self.producto.stock -= self.cantidad
        self.producto.save()
        super(Venta, self).save(*args, **kwargs)

    def __str__(self):
        return f"Venta {self.cod_venta} - {self.cliente.nombre} {self.total}"