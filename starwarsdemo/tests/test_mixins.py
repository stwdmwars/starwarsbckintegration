from datetime import datetime
from django.test import TestCase

from starwarsdemo.apps.core.mixins.models import TimeStampedMixin
from starwarsdemo.tests.models import TimeStampedMock

class TimeStampedMixinTestCase(TestCase):

    def setUp(self):
        self.tsm_instance = TimeStampedMock.objects.create()

    def test_is_abstract(self):
        """ Check if TimeStampedMixin is a abstract Model """

        # pylint: disable=protected-access
        self.assertTrue(TimeStampedMixin._meta.abstract)


    def test_model_has_created_and_updated_fields(self):
        """ Check if fields `created_at` and `updated_at` was implemented in subclass """

        self.assertTrue(hasattr(TimeStampedMock, 'created_at'))
        self.assertTrue(hasattr(TimeStampedMock, 'updated_at'))
        self.assertIs(type(self.tsm_instance.created_at), datetime)
        self.assertIs(type(self.tsm_instance.updated_at), datetime)


    def test_created_at_value_on_add(self):
        """ Check current datetime on `created_at` when edit instance """

        self.assertIsNotNone(self.tsm_instance.created_at)

    def test_updated_at_value_on_edit(self):
        """ Check current datetime on `updated_at` when edit instance """

        self.assertIsNotNone(self.tsm_instance.updated_at)
        self.tsm_instance.save()
        self.assertGreater(
            self.tsm_instance.updated_at,
            self.tsm_instance.created_at
        )


    def tearDown(self):
        self.tsm_instance.delete()
