"""
Geoapp Routes
"""

import requests
from flask import session, Blueprint
from services.api_services import generate_exception_response, generate_success_response, generate_error_response
from services.geoapp_services import GeoAppServices
from wrappers import requires_auth

# set blueprint
geoapp_bp = Blueprint('geoapp_bp', __name__)

# instantiate geoapp services
services = GeoAppServices()


@geoapp_bp.route('/', methods=['GET'])
def index():
    """
    Index
    """
    return 'go to /geoapp/...'


@geoapp_bp.route('/geoapp/zipcode/<string:zipcode>', methods=['GET'])
@requires_auth
def get_paystats_by_zipcode(zipcode: str):
    """
    Get paystats by age and gender given a zipcode

    :param str zipcode: Zip Code
    :return: Paystats dict with aggregated data
    :rtype dict
    """
    try:
        if session.get(zipcode):  # get data from session if already stored
            paystats = session[zipcode]
        else:  # get from db otherwise
            paystats = services.get_paystats_by_zipcode(zipcode=zipcode)
            # store in session
            session[zipcode] = paystats
        if paystats:
            return generate_success_response(code=requests.codes['ok'],
                                             response_data=paystats)
        else:
            return generate_error_response(code=requests.codes['not_found'],
                                           error_message=f"No data found for zipcode {zipcode}")
    except Exception as e:
        return generate_exception_response(exception=e)


@geoapp_bp.route('/geoapp/geometry/<string:geometry>', methods=['GET'])
@requires_auth
def get_paystats_by_geometry(geometry: str):
    """
    Get paystats by age and gender given a WKB geometry

    :param str geometry: WKB
    :return: Paystats dict with aggregated data
    :rtype dict
    """
    try:
        if session.get(geometry):  # get data from session if already stored
            paystats = session[geometry]
        else:  # get from db otherwise
            paystats = services.get_paystats_by_geometry(geometry=geometry)
            # store in session
            session[geometry] = paystats
        if paystats:
            return generate_success_response(code=requests.codes['ok'],
                                             response_data=paystats)
        else:
            return generate_error_response(code=requests.codes['not_found'],
                                           error_message=f"No data found for geometry {geometry}")
    except Exception as e:
        return generate_exception_response(exception=e)


@geoapp_bp.route('/geoapp/all', methods=['GET'])
@requires_auth
def get_all_paystats():
    """
    Get all paystats by age and gender

    :return: Paystats dict with aggregated data
    :rtype dict
    """
    try:
        if session.get('all'):  # get data from session if already stored
            paystats = session['all']
        else:  # get from db otherwise
            paystats = services.get_all_paystats()
            # store in session
            session['all'] = paystats
        if paystats:
            return generate_success_response(code=requests.codes['ok'],
                                             response_data=paystats)
        else:
            return generate_error_response(code=requests.codes['not_found'],
                                           error_message=f"No data found")
    except Exception as e:
        return generate_exception_response(exception=e)
