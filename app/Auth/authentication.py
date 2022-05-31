from requests.auth import HTTPBasicAuth

import requests
from app.Config import PASSWORD_API, USERNAME_API


def basicAuthentication(linkApi):
    try:
        response = requests.get(linkApi, auth=HTTPBasicAuth(USERNAME_API, PASSWORD_API))
        if response.status_code != 200:
            return []
        return response.json()
    except Exception as ex:
        a = 1
