from rest_framework import routers
from .api import ProductoViewSet
from .api import AtributoViewSet
from .api import ClasificacionViewSet
from .api import ProductoAtributoViewSet
from .api import ProductoAllViewSet

router = routers.DefaultRouter()

router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/atributos', AtributoViewSet, 'atributos')
router.register('api/clasificacion', ClasificacionViewSet, 'clasificacion')
router.register('api/producto-atributo', ProductoAtributoViewSet, 'producto-atributo')
router.register('api/producto-all', ProductoAllViewSet, 'producto-all')



urlpatterns = router.urls