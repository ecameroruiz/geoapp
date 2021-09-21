"""
Geoapp routes tests
"""

import base64
import json
import os
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

        # data examples
        cls.test_data = json.load(open(os.path.dirname(os.path.abspath(__file__)) + '/test_data/test_data.json'))

    def test_get_paystats_existing_zipcode(self):
        """
        Test route for existing zipcode
        """
        response = self.client.get(f"/geoapp/zipcode/{self.test_data['existing_zipcode']}", headers=self.headers)
        self.assertEqual(response.status_code, requests.codes['ok'])

    def test_get_paystats_non_existing_zipcode(self):
        """
        Test route for non existing zipcode
        """
        response = self.client.get(f"/geoapp/zipcode/{self.test_data['non_existing_zipcode']}", headers=self.headers)
        self.assertEqual(response.status_code, requests.codes['not_found'])

    def test_get_paystats_existing_geometry(self):
        """
        Test route for existing zipcode
        """
        response = self.client.get(f"/geoapp/geometry/{self.test_data['existing_geometry']}", headers=self.headers)
        self.assertEqual(response.status_code, requests.codes['ok'])

    def test_get_paystats_non_existing_geometry(self):
        """
        Test route for non existing zipcode
        """
        response = self.client.get(f"/geoapp/geometry/{self.test_data['non_existing_geometry']}", headers=self.headers)
        self.assertEqual(response.status_code, requests.codes['not_found'])

    def test_get_all_paystats(self):
        """
        Test route for all paystats
        """
        response = self.client.get(f"/geoapp/all", headers=self.headers)
        self.assertEqual(response.status_code, requests.codes['ok'])
