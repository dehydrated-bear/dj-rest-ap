from rest_framework.routers import DefaultRouter

from product.viewsets import ProductGenericViewSet

router = DefaultRouter()
router.register('products',ProductGenericViewSet,basename='products')

print(router.urls)
urlpatterns=router.urls



