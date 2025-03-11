from django.urls import path
from django.contrib import admin
from smart_home.measurement.views import MeasurementViewSet, SensorViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensor/', SensorViewSet.as_view()),
    path('measurement/', MeasurementViewSet.as_viwe())
]
