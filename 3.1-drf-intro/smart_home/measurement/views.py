# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics

from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurementSerializer, SensorSerializer


# Создать датчик. Указываются название и описание датчика.
class SensorView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer




# Изменить датчик. Указываются название и описание.
class SensorUpView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Добавить измерение. Указываются ID датчика и температура.
class MeasurementView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.
class SensorAllView(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Получить информацию по конкретному датчику. Выдаётся полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем.

