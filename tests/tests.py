"""
Geoapp routes tests
"""

import base64
from unittest import TestCase
from init import create_app
from services.geoapp_services import GeoAppServices
import requests


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

        # set auth headers TODO: credentials should be read from a file
        valid_credentials = base64.b64encode(b"test_username:test_password").decode("utf-8")
        cls.headers = {'Authorization': 'Basic ' + valid_credentials}

    def test_get_paystats_existing_zipcode(self):
        """
        Test route for existing zipcode
        """
        existing_zipcode = '28008'
        response = self.client.get(f"/geoapp/zipcode/{existing_zipcode}", headers=self.headers)
        self.assertEqual(response.status_code, requests.codes['ok'])

    def test_get_paystats_non_existing_zipcode(self):
        """
        Test route for non existing zipcode
        """
        non_existing_zipcode = '00000'
        response = self.client.get(f"/geoapp/zipcode/{non_existing_zipcode}", headers=self.headers)
        self.assertEqual(response.status_code, requests.codes['not_found'])
