from rest_framework import serializers

from starwarsdemo.apps.planets.models import Planet


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    films = serializers.ReadOnlyField()
    films_appearances = serializers.ReadOnlyField()

    class Meta:
        model = Planet
        fields = (
            'pk',
            'url',
            'name',
            'climate',
            'terrain',
            'films',
            'films_appearances',
            'created_at',
            'updated_at'
        )
