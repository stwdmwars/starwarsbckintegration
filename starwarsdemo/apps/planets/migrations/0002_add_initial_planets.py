# Generated by Django 2.1.7 on 2019-02-25 00:38

from django.db import migrations

def add_initial_planets(apps, _schema):
    """
    Add Coruscant, Geonosis and Mygeeto planets
    """
    planet_model = apps.get_model('planets', 'Planet')
    planet_model.objects.bulk_create([
        planet_model(
            pk=1,
            name='Coruscant',
            climate='temperate',
            terrain='cityscape, mountains'
        ),
        planet_model(
            pk=2,
            name='Geonosis',
            climate='temperate, arid',
            terrain='rock, desert, mountain, barren'
        ),
        planet_model(
            pk=3,
            name='Mygeeto',
            climate='frigid',
            terrain='glaciers, mountains, ice canyons'
        )
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_planets)
    ]
