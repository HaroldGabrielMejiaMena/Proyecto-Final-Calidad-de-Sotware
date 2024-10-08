import requests
import json
import config

def post_create_a_department(headers, name, country_id):
    url = f"{config.BASE_URL_BE}/Department"
    payload = {
        "name": name,
        "countryId": country_id
    }
    response = requests.post(url, headers=headers, json=payload)
    return response

def put_update_department(headers, department_id, name, country_id):
    url = f"{config.BASE_URL_BE}/Department"
    payload = json.dumps({
        "departmentId": department_id,
        "name": name,
        "countryId": country_id
    })
    response = requests.put(url, headers=headers, data=payload)
    return response

def delete_department(headers, department_id):
    url = f"{config.BASE_URL_BE}/Department/{department_id}"
    response = requests.delete(url, headers=headers)
    return response

def get_department_by_id(headers, department_id):
    url = f"{config.BASE_URL_BE}/Department/{department_id}"
    response = requests.get(url, headers=headers)
    return response


def get_filtered_departments(headers, country_id):
    url = f"{config.BASE_URL_BE}/Department/getByCountryId/{country_id}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error al obtener departamentos. Código de estado: {response.status_code} - {response.text}")
    return response.json()


def get_departament_by_name(headers, department_name, country_id): 
    url = f"{config.BASE_URL_BE}/Department/paginated?Name={department_name}&countryId={country_id}"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Error al obtener department por nombre: {response.status_code} - {response.text}")

    data = response.json()

    if "data" not in data or not data["data"]:
        raise Exception(f"No se encontró el departamento con el nombre: {department_name} en el país {country_id}")

    return data["data"][0]  
