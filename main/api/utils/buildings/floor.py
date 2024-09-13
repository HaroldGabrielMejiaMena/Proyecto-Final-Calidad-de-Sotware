import requests
import json
import config
from main.api.utils.countries.country import get_all_countries


# Crear un floor 
def post_create_floor(headers, name, parFloorTypeId, openingTime, closingTime, cleaningTime, buildingId):
    url = f"{config.BASE_URL_BE}/Floor"
    payload = json.dumps({
        
        "name": name,
        "parFloorTypeId" : parFloorTypeId,
        "openingTime" : openingTime,
        "closingTime" : closingTime,
        "cleaningTime": cleaningTime,
        "buildingId" : buildingId
    })
    response = requests.post(url, headers=headers, data=payload)
    return response


# Obtener todos los floors
def get_floors(headers):
    url = f"{config.BASE_URL_BE}/Floor"
    response = requests.get(url, headers=headers)
    return response

# Obtener un floor por su ID.
def get_floor_by_id(headers, floor_id):
    url = f"{config.BASE_URL_BE}/Floor/{floor_id}"
    response = requests.get(url, headers=headers)
    return response

# Obtener un floor por su nombre.
def get_floor_by_name(headers, floor_name):
    url = f"{config.BASE_URL_BE}/Floor/paginated?Name={floor_name}&Page=1&PageSize=1"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error al obtener floor por nombre: {response.status_code}")

    data = response.json()

    #print(f"Response JSON: {data}")

    if "data" in data:
        if data["data"]:
            return data["data"][0]  
    else:
        raise Exception("No se encontró la clave 'data' en la respuesta.")



# Actualizar un floor
def put_update_floor(headers, name, parFloorTypeId, openingTime, closingTime, cleaningTime, buildingId, floorId):
    url = f"{config.BASE_URL_BE}/Floor"
    payload = json.dumps({
            
        "name": name,
        "parFloorTypeId" : parFloorTypeId,
        "openingTime" : openingTime,
        "closingTime" : closingTime,
        "cleaningTime": cleaningTime,
        "buildingId" : buildingId,
        "floorId": floorId
        })
    response = requests.put(url, headers=headers, data=payload)
    return response


# Eliminar un modelo por ID
def delete_floor(headers, floor_id):
    url = f"{config.BASE_URL_BE}/Floor/{floor_id}"
    response = requests.delete(url, headers=headers)
    return response
