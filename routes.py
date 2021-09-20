"""
Geoapp Routes
"""

import requests
from flask import session, Blueprint
from services.api_services import generate_exception_response, generate_success_response, generate_error_response
from services.geoapp_services import GeoAppServices

# set blueprint
geoapp_bp = Blueprint('geoapp_bp', __name__)

# instantiate geoapp services
services = GeoAppServices()


@geoapp_bp.route('/geoapp/zipcode/<string:zipcode>', methods=['GET'])
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
