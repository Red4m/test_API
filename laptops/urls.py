from rest_framework.routers import DefaultRouter

from laptops import api

router = DefaultRouter()
router.register(r'laptop-modelset', api.LaptopModelViewSet, basename='laptop')
urlpatterns = router.urls
