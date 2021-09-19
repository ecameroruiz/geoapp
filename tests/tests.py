"""
Unit Tests
"""

import json
import os
from unittest import TestCase
from init import create_app
from services.geoapp_services import GeoAppServices
from unittest.mock import MagicMock


class Tests(TestCase):
    """
    Unit Tests
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up testing flask application
        """
        # create app
        cls.app = create_app(config='testing')

        # set test client
        cls.client = cls.app.test_client()

        # set up geoapp services
        cls.movies_api_services_tester = GeoAppServices()

        # read test data
        cls.test_postal_codes = json.load(open(os.path.dirname(os.path.abspath(__file__))
                                               + '/test_data/test_postal_codes.json'))
        cls.test_paystats = json.load(open(os.path.dirname(os.path.abspath(__file__))
                                           + '/test_data/test_paystats.json'))

    def test_get_paystats(self):
        """
        Test get paystats route
        """
        response = self.client.get('/geoapp')
        # check response is correct
        self.assertEqual(response.status_code, 200)

