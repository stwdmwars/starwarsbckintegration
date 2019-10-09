from django.test import TestCase
from django.conf import settings

class SettingsTestCase(TestCase):

    def test_paginator_is_enabled(self):
        """ Check if paginator is enabled to API """

        self.assertIsNotNone(settings.REST_FRAMEWORK)
        self.assertEqual(
            settings.REST_FRAMEWORK['DEFAULT_PAGINATION_CLASS'],
            'rest_framework.pagination.LimitOffsetPagination'
        )


    def test_paginate_20_per_page(self):
        """  Check if paginator allows only 20 items per page """

        self.assertEqual(settings.REST_FRAMEWORK['PAGE_SIZE'], 20)
