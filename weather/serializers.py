from rest_framework import serializers
from .models import WeatherInfo


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherInfo
        fields = ("temp", "city_name", "pressure", "country_code", "wind_speed")
