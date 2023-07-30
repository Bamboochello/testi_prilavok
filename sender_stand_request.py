import data
import configuration
import requests

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER,
                         json=body,
                         headers=data.headers
                         )

def post_new_user_kit(body, headers):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KIT,
                         json=body,
                         headers=headers)
