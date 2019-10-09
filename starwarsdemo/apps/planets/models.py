from django.db import models
from django.utils.text import gettext_lazy as _

from starwarsdemo.apps.core.mixins.models import TimeStampedMixin
from starwarsdemo.apps.swapi.services import SwapiService

class Planet(TimeStampedMixin):

    name = models.CharField(_('Name'), max_length=255, unique=True)
    climate = models.CharField(_('Climate'), max_length=255, default='unknown')
    terrain = models.CharField(_('Terrain'), max_length=255, default='unknown')

    swapi = SwapiService()

    @property
    def films(self):
        return self.swapi.get_films_from_planet(self.name)

    @property
    def films_appearances(self):
        return len(self.films)

    def __str__(self):
        return self.name
