import requests
import json
import config

# Crear un brand
def post_create_brand(headers, name):
    url = f"{config.BASE_URL_BE}/Brand"
    payload = json.dumps({
        "name": name
    })
    response = requests.post(url, headers=headers, data=payload)
    return response

# Obtener todos los brands
def get_brand(headers):
    url = f"{config.BASE_URL_BE}/Brand"
    response = requests.get(url, headers=headers)
    return response

# Obtener un brand por su ID.
def get_brand_by_id(headers, brand_id):
    url = f"{config.BASE_URL_BE}/Brand/{brand_id}"
    response = requests.get(url, headers=headers)
    return response

# Obtener un brand por su nombre.
def get_brand_by_name(headers, brand_name):
    url = f"{config.BASE_URL_BE}/Brand/paginated?Name={brand_name}&Page=1&PageSize=1"
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

# Actualizar un brand
def put_update_brand(headers, brand_id, name):
    url = f"{config.BASE_URL_BE}/Brand"
    payload = json.dumps({
        "name": name,
        "brandId": brand_id
    })
    response = requests.put(url, headers=headers, data=payload)
    return response

# Eliminar un brand por ID
def delete_brand(headers, brand_id):
    url = f"{config.BASE_URL_BE}/Brand/{brand_id}"
    response = requests.delete(url, headers=headers)
    return response
