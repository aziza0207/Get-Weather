from rest_framework.routers import DefaultRouter
from weather.views import WeatherViewSet

router = DefaultRouter()
router.register("", WeatherViewSet, basename="weather")