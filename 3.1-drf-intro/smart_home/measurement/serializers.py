from rest_framework import serializers
from .models import Sensor, Measurement




class SensorModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class MeasurementModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'