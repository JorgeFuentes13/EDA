from rest_framework import serializers
from .models import Producto
from .models import Clasificion
from .models import Atributo
from .models import Producto_Atributo

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ClasificacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clasificion
        fields = '__all__'

class AtributoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Atributo
        fields = '__all__'

class ProductoAtributoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto_Atributo
        fields = '__all__'

class ProductoAllSerializers(serializers.ModelSerializer):
    clasificacion = ClasificacionSerializers(source='clasificacion_id', read_only=True)

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'descripcion', 'precio', 'activo', 'destacado', 'image1', 'clasificacion')