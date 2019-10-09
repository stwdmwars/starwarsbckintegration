from django_filters import rest_framework as filters

from starwarsdemo.apps.planets.models import Planet

class PlanetFilter(filters.FilterSet):
    """
    `PlanetFilter` allow to filtering in `starwarsdemo.Planet` model
    fields `name`, `climate` and `terrain` by using
    `icontains` Lookup.

    Also, `PlanetFilter` provides `iexact` Lookup filtering, by just add
    `__exact` sufix in field name. E.g: `name__exact`
    """
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    name__exact = filters.CharFilter(field_name='name', lookup_expr='iexact')

    climate = filters.CharFilter(field_name='climate', lookup_expr='icontains')
    climate__exact = filters.CharFilter(field_name='climate', lookup_expr='iexact')

    terrain = filters.CharFilter(field_name='terrain', lookup_expr='icontains')
    terrain__exact = filters.CharFilter(field_name='terrain', lookup_expr='iexact')

    class Meta:
        model = Planet
        exclude = ['id', 'created_at', 'updated_at']
