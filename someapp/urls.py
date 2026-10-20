from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import NumberViewSet

router = DefaultRouter()
router.register('numbers', NumberViewSet)

urlpatterns = router.get_urls()
=======
from .views import ManufacturerViewset, ProductViewset

router = DefaultRouter()
router.register('manufacturer', ManufacturerViewset)
router.register('product', ProductViewset)


urlpatterns = router.get_urls()


>>>>>>> a843fd4bf8dd8d9ec65f41d812ecbd6bfe41a75b
