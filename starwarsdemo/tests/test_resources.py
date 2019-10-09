from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from starwarsdemo.apps.planets.models import Planet
from starwarsdemo.apps.planets.serializers import PlanetSerializer
from starwarsdemo.apps.planets.viewsets import PlanetViewSet


class PlanetsResourceTestCase(APITestCase):
    path = '/api/planets/'
    factory = APIRequestFactory()


    def object_url(self, object_id):
        return "%s%i" % (self.path, object_id)


    @classmethod
    def setUpClass(cls):
        Planet.objects.bulk_create([
            Planet(
                name='Hoth',
                climate='frozen',
                terrain='tundra, ice caves, mountain ranges'
            ),
            Planet(
                name='Tatooine',
                climate='arid',
                terrain='desert'
            ),
            Planet(
                name='Jakku',
                climate='unknown',
                terrain='deserts'
            ),
        ])

    def test_planet_resource_is_avaliable(self):
        """ Check if planets resource is available """

        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_planet_list(self):
        """ GET planets """

        request = self.factory.get(self.path)
        planets = Planet.objects.all()
        serializer = PlanetSerializer(
            planets,
            many=True,
            context={'request': request}
        )
        planet_list = PlanetViewSet.as_view({'get': 'list'})
        response = planet_list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)


    def test_planet_retrieve(self):
        """ GET planet object """

        planet = Planet.objects.first()
        request = self.factory.get(self.object_url(planet.pk))
        serializer = PlanetSerializer(
            planet,
            context={'request': request}
        )
        planet_retrieve = PlanetViewSet.as_view({'get': 'retrieve'})
        response = planet_retrieve(request, pk=planet.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


    def test_create_planet(self):
        """ POST planets """

        data = {
            "name": "Polis Massa",
            "climate": "artificial temperate",
            "terrain": "airless asteroid"
        }
        request = self.factory.post(self.path, data=data)
        planet_create = PlanetViewSet.as_view({'post': 'create'})
        response = planet_create(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Planet.objects.filter(name="Polis Massa").exists())


    def test_update_planet(self):
        """ PUT planet """

        planet = Planet.objects.create(
            name="x",
            climate="y",
            terrain="x"
        )
        new_data = {
            "name":"Rodia",
            "climate":"hot",
            "terrain":"jungles, oceans, urban, swamps"
        }
        request = self.factory.put(self.object_url(planet.pk), data=new_data)
        planet_update = PlanetViewSet.as_view({'put': 'update'})
        response = planet_update(request, pk=planet.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Planet.objects.filter(name="Rodia").exists())


    def test_partial_update_planet(self):
        """ PATCH planet """

        planet = Planet.objects.last()
        new_data = {
            "terrain":"a nice great terrain"
        }
        request = self.factory.patch(self.object_url(planet.pk), data=new_data)
        planet_partial_update = PlanetViewSet.as_view({'patch': 'partial_update'})
        response = planet_partial_update(request, pk=planet.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Planet.objects.filter(terrain=new_data['terrain']).exists())


    def test_delete_planet(self):
        """ DELETE planet """

        planet = Planet.objects.last()
        request = self.factory.delete(self.object_url(planet.pk))
        planet_destoy = PlanetViewSet.as_view({'delete': 'destroy'})
        response = planet_destoy(request, pk=planet.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Planet.objects.filter(pk=planet.pk).exists())


    def test_search_planet_by_name(self):
        """ Get planet by name """

        planet = Planet.objects.first()
        request = self.factory.get("%s?name=%s" % (self.path, planet.name.lower()))
        serializer = PlanetSerializer(
            planet,
            context={'request': request}
        )
        planet_list = PlanetViewSet.as_view({'get': 'list'})
        response = planet_list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(next(iter(response.data['results'])), serializer.data)


    def test_search_planet_by_name_exact(self):
        """ Get planet by name with exact lookup"""

        planet = Planet.objects.get(name__iexact='Tatooine')
        request = self.factory.get("%s?name__exact=%s" % (self.path, planet.name))
        serializer = PlanetSerializer(
            planet,
            context={'request': request}
        )
        planet_list = PlanetViewSet.as_view({'get': 'list'})
        response = planet_list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(next(iter(response.data['results'])), serializer.data)


    def test_search_planet_by_climate(self):
        """ Get planet by climate """

        planet = Planet.objects.get(climate='arid')
        request = self.factory.get("%s?climate=%s" % (self.path, planet.climate))
        serializer = PlanetSerializer(
            planet,
            context={'request': request}
        )
        planet_list = PlanetViewSet.as_view({'get': 'list'})
        response = planet_list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(serializer.data, response.data['results'])


    def test_search_planet_by_terrain(self):
        """ Get planet by terrain """

        planet = Planet.objects.get(terrain='deserts')
        request = self.factory.get("%s?terrain=%s" % (self.path, planet.terrain))
        serializer = PlanetSerializer(
            planet,
            context={'request': request}
        )
        planet_list = PlanetViewSet.as_view({'get': 'list'})
        response = planet_list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(serializer.data, response.data['results'])


    def test_planet_have_films_field(self):
        """ Check if films list is present in planet object """

        planet = Planet.objects.get(name="Tatooine")
        request = self.factory.get(self.object_url(planet.pk))
        planet_retrieve = PlanetViewSet.as_view({'get': 'retrieve'})
        response = planet_retrieve(request, pk=planet.pk)
        self.assertTrue('films' in response.data.keys())
        self.assertIsInstance(response.data['films'], list)


    def test_planet_films_appearances_calc(self):
        """ Check field films_appearances is properly calculated """

        planet = Planet.objects.get(name="Jakku")
        planet_films = [
            "https://swapi.co/api/films/7/"
        ]
        request = self.factory.get(self.object_url(planet.pk))
        planet_retrieve = PlanetViewSet.as_view({'get': 'retrieve'})
        response = planet_retrieve(request, pk=planet.pk)
        self.assertTrue('films_appearances' in response.data.keys())
        self.assertIsInstance(response.data['films_appearances'], int)
        self.assertEqual(response.data['films_appearances'], len(planet_films))



    @classmethod
    def tearDownClass(cls):
        Planet.objects.all().delete()
