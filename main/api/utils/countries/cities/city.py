import requests
import json
import config


def post_create_a_city(headers, name, available, country_id):
    # Crear el payload manualmente como diccionario antes de convertirlo a JSON
    payload = {
        "name": name,
        "available": available,
        "countryId": country_id
    }
    
    # Serializa el payload a JSON correctamente
    payload_json = json.dumps(payload)

    # Hacer la solicitud POST
    url = f"{config.BASE_URL_BE}/City"
    response = requests.post(url, headers=headers, data=payload_json)
    return response


def put_update_city(headers, city_id, name, available, country_id):
    url = f"{config.BASE_URL_BE}/City"
    payload = json.dumps({
        "id": city_id,
        "name": name,
        "available": available,
        "countryId": country_id
    })
    response = requests.put(url, headers=headers, data=payload)
    return response


def get_city_by_id(headers, city_id):
    url = f"{config.BASE_URL_BE}/City/{city_id}"
    response = requests.get(url, headers=headers)
    return response 


def delete_city(headers, city_id):
    url = f"{config.BASE_URL_BE}/City/{city_id}"
    response = requests.delete(url, headers=headers)
    return response


def get_filtered_cities(headers, name=None, available=None):
    url = f"{config.BASE_URL_BE}/City/filtered"
    params = {}
    if name:
        params["name"] = name
    if available is not None:
        params["available"] = available
    
    response = requests.get(url, headers=headers, params=params)
    return response.json()


def get_paginated_cities(headers, page_number=1, page_size=10):
    url = f"{config.BASE_URL_BE}/City/paginated"
    params = {
        "pageNumber": page_number,
        "pageSize": page_size
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()