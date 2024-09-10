import requests
import json
import config
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200


def post_create_a_country(headers, name, available):

        url = f"{config.BASE_URL_BE}/Country"

        payload = json.dumps({
            "available": available,
            "name": name,
            "cities": []
        })

        response = requests.post(url, headers=headers, data=payload)
        return response

    

def get_country_by_id(headers, country_id):
        url = f"{config.BASE_URL_BE}/Country/{country_id}"
        response = requests.get(url, headers=headers)
        return response.json()

    
def put_update_country(headers, country_id, name, available):
        url = f"{config.BASE_URL_BE}/Country"
        payload = json.dumps({
            "id": country_id,
            "name": name,
            "available": available,
        })
        response = requests.put(url, headers=headers, data=payload)
        return response

    
def delete_country(headers, country_id):
        url = f"{config.BASE_URL_BE}/Country/{country_id}"
        response = requests.delete(url, headers=headers)
        return response


def get_filtered_countries(headers, name=None, available=None):
        url = f"{config.BASE_URL_BE}/Country/filtered"
        params = {}
        if name:
            params["name"] = name
        if available is not None:
            params["available"] = available
        
        response = requests.get(url, headers=headers, params=params)
        return response.json() 
    
def get_filtered_country(headers, name=None, available=None):
    url = f"{config.BASE_URL_BE}/Country/filtered"
    params = {}

    # Agregar los filtros basados en los parámetros recibidos
    if name:
        params["name"] = name
    if available is not None:
        params["available"] = available

    response = requests.get(url, headers=headers, params=params)
    # Verifica que la respuesta sea exitosa
    if response.status_code != 200:
        raise Exception(f"Error en la solicitud de filtrado: {response.status_code}")
    
    # Retorna la respuesta en formato JSON
    return response.json()