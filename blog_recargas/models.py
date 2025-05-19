from django.db import models

class EmpresaRecarga(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Recarga(models.Model):
    monto = models.DecimalField(max_digits=6, decimal_places=2)
    telefono = models.CharField(max_length=10)
    empresa = models.ForeignKey(EmpresaRecarga, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recarga de ${self.monto} a {self.telefono} ({self.empresa})"