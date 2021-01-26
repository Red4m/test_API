from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from employee import api

router = DefaultRouter()
router.register(r'employee-modelset', api.EmployeeModelViewSet, basename='employee')
urlpatterns = router.urls
