"""
API Services
"""

import json
import sys
import requests


def generate_success_response(code, response_data):
    """
    Generate API success response

    :param int code: Success code
    :param response_data: JSON response to return
    """
    content_type = {'Content-Type': 'application/json'}
    return json.dumps(response_data), code, content_type


def generate_error_response(code, error_message):
    """
    Generate API error response

    :param int code: Error code
    :param str error_message: Error message for response
    """
    content_type = {'Content-Type': 'application/json'}
    print(error_message)
    return json.dumps(error_message), code, content_type


def generate_exception_response(exception, error_message=''):
    """
    Generate API exception response

    :param str error_message: Error message for response
    :param Exception exception: Exception that occurred
    """
    print(exception, file=sys.stderr)
    print(error_message)
    return generate_error_response(code=requests.codes['internal_server_error'], error_message=error_message)
