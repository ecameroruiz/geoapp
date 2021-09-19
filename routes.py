"""
Geoapp Routes
"""

import requests
from flask import session, Blueprint
from services.api_services import generate_exception_response, generate_error_response, generate_success_response
from services.geoapp_services import GeoAppServices

# set blueprint
geoapp_bp = Blueprint('geoapp_bp', __name__)

# instantiate geoapp services
services = GeoAppServices()


@geoapp_bp.route('/', methods=['GET'])
def index():
    """
    Index
    """
    return 'Go to /geoapp route to display movie list'


@geoapp_bp.route('/geoapp', methods=['GET'])
def get_data():
    """
    Description
    """
    try:
        paystats = services.get_paystats()
        return generate_success_response(code=requests.codes['ok'], response_data=paystats)
    except Exception as e:
        return generate_exception_response(exception=e, error_message='An error occurred when processing the request')
