"""
Registration Routes
"""

import requests
from flask import Blueprint, request
from services.api_services import generate_exception_response, generate_success_response, generate_error_response
from services.authorization_services import AuthorizationServices

# set blueprint
registration_bp = Blueprint('registration_bp', __name__)

# get service
authorization_services = AuthorizationServices()


@registration_bp.route('/registration/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    try:
        # check arguments are given
        if username is None or password is None:
            return generate_error_response(code=requests.codes['bad_request'],
                                           error_message="Missing username or password")
        # check user is already on db
        if authorization_services.check_user_exists(username=username):
            return generate_error_response(code=requests.codes['bad_request'],
                                           error_message=f"User {username} already exists")
        # save user to db
        authorization_services.save_user(username=username, password=password)
        return generate_success_response(code=requests.codes['created'],
                                         response_data=f"User {username} successfully registered")
    except Exception as e:
        return generate_exception_response(exception=e)
