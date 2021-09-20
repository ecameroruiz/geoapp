"""
Application Wrappers
"""

from functools import wraps
import requests
from flask import request
from services.api_services import generate_error_response
from services.authorization_services import AuthorizationServices

# get service
authorization_services = AuthorizationServices()


def requires_auth(f):
    """
    Wrapper to verify authorization with username and password
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):

        # get credentials
        username = request.authorization.get('username')
        password = request.authorization.get('password')

        # check credentials
        credentials_provided = username and password

        # verify user's permissions
        verification_response = credentials_provided and authorization_services.verify_user(username=username, password=password)

        if verification_response:  # proceed if user is verified
            return f(*args, **kwargs)
        else:  # abort if user doesn't have required permissions
            return generate_error_response(code=requests.codes['unauthorized'], error_message='Authentication failed')

    return decorated_function
