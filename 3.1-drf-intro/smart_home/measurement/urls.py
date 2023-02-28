from django.urls import path

from measurement.views import MeasurementView, SensorAllView, SensorUpView, SensorView

urlpatterns = [
   path('crsensor/', SensorView.as_view(), name='create_sensor'),
   path('upsensor/<pk>/', SensorUpView.as_view(), name ='update_sensor'),
   path('crmeasurement/', MeasurementView.as_view(), name ='create_measurement'),
   path('allsensors/', SensorAllView.as_view(), name = 'all_sensors'),
   path('allsensors/<pk>/', SensorAllView.as_view(), name = 'sensor'),

]
