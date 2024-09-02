import requests
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import config


url = "http://host.docker.internal:8083/connect/token"

# Definiendo el payload como un diccionario
payload = {
    'grant_type': 'authorization_code',
    'username': config.USERNAME,
    'password': config.PASSWORD,
    'scope': 'openid roles profile dashboard',
    'client_id': 'adas-v2-spa',
    'redirect_uri': 'http://localhost:3033/auth/login-oidc'
}

# Si necesitas agregar más campos, simplemente añádelos al diccionario
# payload['nuevo_campo'] = 'valor'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Convertir el diccionario a un formato adecuado para una solicitud POST
response = requests.post(url, headers=headers, data=payload)

print(response.text)
