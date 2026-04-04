from django.db import models


# Create your models here.

class EstatusPruebas(models.Model):
    IdEstatusPrueba = models.AutoField(primary_key=True)
    NombreEstatusPrueba = models.CharField(max_length=30)
    Activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.NombreEstatusPrueba}"
    
class TiposPruebas(models.Model):
    IdTipoPrueba = models.AutoField(primary_key=True)
    NombreTipoPrueba = models.CharField(max_length=30)
    Activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.NombreTipoPrueba}"
    
class Pruebas(models.Model):
    IdPrueba = models.AutoField(primary_key=True)
    IdTester = models.ForeignKey('usuarios.Testers' , on_delete=models.CASCADE)
    IdEstatusPrueba = models.ForeignKey(EstatusPruebas, on_delete=models.CASCADE)
    IdTipoPrueba = models.ForeignKey(TiposPruebas, on_delete=models.CASCADE)
    CodigoPrueba = models.CharField(max_length=10)
    NombrePrueba = models.CharField(max_length=50)
    IdentificadorPrueba = models.CharField(max_length=30, null=True)
    ComentariosPrueba = models.CharField(max_length=100)
    FechaAlta = models.DateField()
    FechaInicio = models.DateField()
    FechaFin = models.DateField()
    
    def __str__(self):
        return f"{self.CodigoPrueba} {self.NombrePrueba}"
    