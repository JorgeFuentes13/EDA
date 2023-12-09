from .models import Producto
from .models import Clasificion
from .models import Atributo
from .models import Producto_Atributo
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializers
from .serializers import ClasificacionSerializers
from .serializers import AtributoSerializers
from .serializers import ProductoAtributoSerializers
from .serializers import ProductoAllSerializers

from django.db.models import F


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializers

class ClasificacionViewSet(viewsets.ModelViewSet):
    queryset = Clasificion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClasificacionSerializers

class AtributoViewSet(viewsets.ModelViewSet):
    queryset = Atributo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AtributoSerializers

class ProductoAtributoViewSet(viewsets.ModelViewSet):
    queryset = Producto_Atributo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoAtributoSerializers

class ProductoAllViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.select_related('clasificacion_id').all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoAllSerializers

