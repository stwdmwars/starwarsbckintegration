from django.test import TestCase
from django.db import IntegrityError

from starwarsdemo.apps.planets.models import Planet

class PlanetTestCase(TestCase):

    def test_create_planet(self):
        """ Tries to create a planet """

        planet = Planet(
            name="Alderaan",
            climate="temperate",
            terrain="grasslands, mountains"
        )
        planet.save()
        self.assertEqual(Planet.objects.last().pk, planet.pk)


    def test_update_planet(self):
        """ Tries to update a planet """

        planet = Planet.objects.create(
            name="Dagobah",
            climate="murky",
            terrain="plain"
        )
        planet.terrain = "swamp, jungle"
        planet.save()
        self.assertEqual(Planet.objects.last().terrain, planet.terrain)


    def test_delete_planet(self):
        """ Tries to delete a planet """
        planet = Planet.objects.create(
            name="Dagobah",
            climate="murky",
            terrain="plain"
        )
        planet.delete()
        self.assertNotIn(planet, Planet.objects.all())

    def test_planet_str_representation(self):
        """ Check __str__ method is present """

        planet = Planet(
            name="Stewjon",
            climate="temperate",
            terrain="grass"
        )
        self.assertEqual(str(planet), planet.name)

    def test_prevent_create_duplicated_planet(self):
        """ Prevent to create two planets with same name """

        with self.assertRaises(IntegrityError):
            planet_a = Planet(
                name="a",
                climate="x",
                terrain="y",
            )
            planet_a.save()
            Planet.objects.create(
                name=planet_a.name,
                climate="z",
                terrain="v"
            )
