from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'measurements', views.MeasurementViewSet, base_name="measurements")


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
