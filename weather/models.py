from django.db import models
from django.utils.translation import gettext_lazy as _


class WeatherInfo(models.Model):
    city_id = models.IntegerField(_("Код города"))
    city_name = models.CharField(_("Город"), max_length=255)
    temp = models.CharField(_("Температура"), max_length=10)
    wind_speed = models.SmallIntegerField(_("Скорость ветра"))
    country_code = models.CharField(_("Код страны"), max_length=5)
    pressure = models.SmallIntegerField(_("Давление"))
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    date_updated = models.DateTimeField("Дата редактирования", auto_now=True)

    class Meta:
        verbose_name = "Прогноз погоды"
        verbose_name_plural = "Прогноз погоды"

