from rest_framework.routers import DefaultRouter

from product.viewset import ProductViewSet


router = DefaultRouter()

router.register('product-abc',ProductViewSet,basename='product')


print(router.urls)
urlpatterns = router.urls