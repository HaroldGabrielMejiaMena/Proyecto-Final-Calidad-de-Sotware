import requests
import json
import config
from main.api.utils.countries.country import get_all_countries


# Crear un building 
def post_create_building(headers, name, country_id, direction, cityId):
    url = f"{config.BASE_URL_BE}/Building"
    payload = json.dumps({
        
        "softwareCenter": [country_id, cityId],
        "name": name,
        "direction": direction,
        "cityId": cityId
    })
    response = requests.post(url, headers=headers, data=payload)
    return response


# Obtener todos los buildings
def get_building(headers):
    url = f"{config.BASE_URL_BE}/Building"
    response = requests.get(url, headers=headers)
    return response

# Obtener un building por su ID.
def get_building_by_id(headers, building_id):
    url = f"{config.BASE_URL_BE}/Building/{building_id}"
    response = requests.get(url, headers=headers)
    return response

# Obtener un building por su nombre.
def get_building_by_name(headers, building_name):
    url = f"{config.BASE_URL_BE}/Building/paginated?Name={building_name}&Page=1&PageSize=1"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error al obtener brand por nombre: {response.status_code}")

    data = response.json()

    #print(f"Response JSON: {data}")

    if "data" in data:
        if data["data"]:
            return data["data"][0]  
    else:
        raise Exception("No se encontró la clave 'data' en la respuesta.")



# Actualizar un building
def put_update_building(headers, name, country_id, direction, cityId, buildingId):
    url = f"{config.BASE_URL_BE}/Building"
    payload = json.dumps({
        "softwareCenter": [country_id, cityId],
        "name": name,
        "direction": direction,
        "cityId": cityId,
        "buildingId": buildingId
    })
    response = requests.put(url, headers=headers, data=payload)
    return response


# Eliminar un modelo por ID
def delete_building(headers, building_id):
    url = f"{config.BASE_URL_BE}/Building/{building_id}"
    response = requests.delete(url, headers=headers)
    return response


# Obtener todos los modelos y devolver los assetTypeIds
def get_software_center(headers):
    url = f"{config.BASE_URL_BE}/ModModel"
    response = requests.get(url, headers=headers)
    
    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200, f"Error al obtener los modelos: {response.status_code} - {response.text}"
    
    # Parsear el JSON de la respuesta
    models_data = response.json()
    
    # Extraer todos los assetTypeId de la respuesta
    asset_type_ids = [model["assetType"]["assetTypeId"] for model in models_data if model.get("assetType")]
    
    # Verificar que se encontraron assetTypeIds
    assert len(asset_type_ids) > 0, "No se encontraron assetTypeIds en la respuesta"
    
    return asset_type_ids


# Método para obtener un country y un city válidos desde la respuesta de get_all_countries
def get_valid_country_and_city(headers):
    response = get_all_countries(headers)
    assert response.status_code == 200, f"Error al obtener countries: {response.status_code} - {response.text}"
    
    countries_data = response.json()["data"]
    
    # Filtrar un country que tenga cities disponibles
    for country in countries_data:
        if country["available"] and len(country["cities"]) > 0:
            for city in country["cities"]:
                if city["available"]:
                    return country["id"], city["id"]  # Retornar el country_id y city_id
    
    raise Exception("No se encontró un country con cities disponibles para la actualización")

