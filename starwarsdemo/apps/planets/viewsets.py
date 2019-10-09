from rest_framework import viewsets

from starwarsdemo.apps.planets.models import Planet
from starwarsdemo.apps.planets.serializers import PlanetSerializer
from starwarsdemo.apps.planets.filters import PlanetFilter

# pylint: disable=too-many-ancestors
class PlanetViewSet(viewsets.ModelViewSet):
    """
    Planets API resource
    """
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    filter_class = PlanetFilter
