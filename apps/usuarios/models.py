from django.db import models

# Create your models here.

class Testers(models.Model):
    IdTester = models.AutoField(primary_key=True)
    NombreTester = models.CharField(max_length=30)
    ApellidoPaterno = models.CharField(max_length=30)
    ApellidoMaterno = models.CharField(max_length=30, null=True, )
    Activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.NombreTester} {self.ApellidoPaterno}"
