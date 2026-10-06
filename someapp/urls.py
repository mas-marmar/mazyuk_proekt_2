from rest_framework.routers import DefaultRouter
from .views import ManufacturerViewset, ProductViewset

router = DefaultRouter()
router.register('manufacturer', ManufacturerViewset)
router.register('product', ProductViewset)


urlpatterns = router.get_urls()


