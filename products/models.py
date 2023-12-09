from django.db import models

# Create your models here.

class Clasificion(models.Model):
        nombre = models.CharField(max_length=200)

        def __str__(self):
                return self.nombre
        
        class Meta:
                db_table = 'Clasificacion'

class Producto(models.Model):
        nombre = models.CharField(max_length=200)
        descripcion = models.TextField()
        precio = models.IntegerField()
        activo = models.BooleanField(default= True)
        destacado = models.BooleanField(default= False)
        image1 = models.CharField(max_length=200,default='-')
        clasificacion_id = models.ForeignKey(Clasificion, on_delete=models.CASCADE)

        def __str__(self):
                return self.nombre

        class Meta:
                db_table = 'Producto'

class Atributo(models.Model):
        nombre = models.CharField(max_length=200)

        def __str__(self):
                return self.nombre
        
        class Meta:
                db_table = 'Atributo'


class Producto_Atributo(models.Model):
        valor_atributo = models.CharField(max_length=200)
        atributo_id =  models.ForeignKey(Atributo, on_delete=models.CASCADE)
        producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)

        class Meta:
                db_table = 'Producto_Atributo'