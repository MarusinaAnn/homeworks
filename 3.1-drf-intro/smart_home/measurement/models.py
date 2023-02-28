from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100, blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temp = models.DecimalField(max_digits=4, decimal_places=1)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True)