import requests
import ui_config
from main.api.assertions.general_assertions.status_code import assert_get_status_code_200
def get_response_connect_token():
    url = "http://host.docker.internal:8083/connect/token"

    payload = {
        'grant_type': 'password',
        'username': ui_config.USERNAME,
        'password': ui_config.PASSWORD,
        'scope': 'openid roles profile adas-v2-api',
        'client_id': 'adas-v2-spa'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert_get_status_code_200(response)
    return response.json()

def get_token():
    response_data = get_response_connect_token()
    token = response_data.get("access_token", None)
    return token
    
