import requests
import json
import config


def post_create_a_country(headers, name, available):
        url = f"{config.BASE_URL_BE}/Country"
        payload = json.dumps({
            "available": available,
            "name": name,
            "cities": []
        })
        response = requests.post(url, headers=headers, data=payload)
        return response

def get_all_countries(headers):
        url = f"{config.BASE_URL_BE}/Country/paginated"
        response = requests.get(url, headers=headers)
        return response

    

def get_country_by_id(headers, country_id):
        url = f"{config.BASE_URL_BE}/Country/{country_id}"
        response = requests.get(url, headers=headers)
        return response
    
    
def get_country_by_name(headers, country_name):
    url = f"{config.BASE_URL_BE}/Country/paginated?Name={country_name}&Page=1&PageSize=1"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error al obtener country por nombre: {response.status_code}")
    data = response.json()
    if "data" in data:
        if data["data"]:
            return data["data"][0]  
    else:
        raise Exception("No se encontró la clave 'data' en la respuesta.")

    
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
    if name:
        params["name"] = name
    if available is not None:
        params["available"] = available
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Error en la solicitud de filtrado: {response.status_code}")
    return response.json()


def get_first_country_id(headers):
    url = f"{config.BASE_URL_BE}/Country/paginated"
    response = requests.get(url, headers=headers)

    data = response.json().get("data", [])
    
    if len(data) == 0:
        raise Exception("No se encontraron países en la respuesta")

    return data[0]["id"]

