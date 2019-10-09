from django.urls import include, path
from django.views.generic.base import RedirectView
from rest_framework import routers

from starwarsdemo.apps.planets.viewsets import PlanetViewSet

router = routers.DefaultRouter()
router.register(r'planets', PlanetViewSet)


urlpatterns = [

    # Automatic URL mapping for registered resources
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='api/', permanent=False)),
]
