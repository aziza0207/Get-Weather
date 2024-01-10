import requests
import datetime
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.utils.timezone import now
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import WeatherInfo
from .serializers import WeatherSerializer
from rest_framework import status


class WeatherViewSet(viewsets.ViewSet):
    serializer_class = WeatherSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="city",
                description="Город",
                required=True,
                type=OpenApiTypes.STR,
            ),
        ]
    )

    @action(detail=False, methods=["GET"])
    def weather(self, request):
        try:
            city = request.query_params.get("city")
            weather_info = WeatherInfo.objects.filter(city_name=city).first()

            if weather_info is None or weather_info.date_updated < now() - datetime.timedelta(minutes=30):

                res = requests.get(
                    "http://api.openweathermap.org/data/2.5/find",
                    params={
                        "q": city,
                        "units": "metric",
                        "APPID": "161723404a43d1c2cac144340b51f3e5",
                    },
                )
                data = res.json()["list"][0]

                city_id = data["id"]
                city_name = data["name"]
                pressure = data["main"]["pressure"]
                temp = data["main"]["temp"]
                wind = data["wind"]["speed"]
                country = data["sys"]["country"]

                weather_info, created = WeatherInfo.objects.update_or_create(
                    city_name=city_name,
                    defaults={
                        "city_id": city_id,
                        "temp": temp,
                        "wind_speed": wind,
                        "country_code": country,
                        "pressure": pressure,

                    }
                )

            serializer = WeatherSerializer(weather_info)
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
