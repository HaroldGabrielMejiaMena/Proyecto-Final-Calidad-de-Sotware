import requests
import json
import config

# Crear un modelo comercial
def post_create_comercial_model(headers, name, assetTypeId, parModelTypeId, modCommercialModelId):
    url = f"{config.BASE_URL_BE}/ModModel"
    payload = json.dumps({
        "name": name,
        "assetTypeId": assetTypeId,
        "parModelTypeId": parModelTypeId,
        "modCommercialModelId": modCommercialModelId
    })
    response = requests.post(url, headers=headers, data=payload)
    return response

# Crear un modelo de fabrica
def post_create_factory_model(headers, name, assetTypeId, parModelTypeId, modCommercialModelId):
    url = f"{config.BASE_URL_BE}/ModModel"
    payload = json.dumps({
        "name": name,
        "assetTypeId": assetTypeId,
        "parModelTypeId": parModelTypeId,
        "modCommercialModelId": modCommercialModelId
    })
    response = requests.post(url, headers=headers, data=payload)
    return response

# Obtener todos los modelos
def get_models(headers):
    url = f"{config.BASE_URL_BE}/ModModel"
    response = requests.get(url, headers=headers)
    return response

# Obtener un modelo por su ID.
def get_model_by_id(headers, model_id):
    url = f"{config.BASE_URL_BE}/ModModel/{model_id}"
    response = requests.get(url, headers=headers)
    return response

# Obtener un modelo por su nombre.
def get_model_by_name(headers, model_name):
    url = f"{config.BASE_URL_BE}/ModModel/paginated?Name={model_name}&Page=1&PageSize=1"
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

# Actualizar un modelo comercial
def put_update_comercial_model(headers, name, assetTypeId, parModelTypeId, modCommercialModelId, modelId):
    url = f"{config.BASE_URL_BE}/ModModel"
    payload = json.dumps({
        "name": name,
        "assetTypeId": assetTypeId,
        "parModelTypeId": parModelTypeId,
        "modCommercialModelId": modCommercialModelId, 
        "modelId": modelId
    })
    response = requests.put(url, headers=headers, data=payload)
    return response


# Actualizar un modelo de fabrica
def put_update_factory_model(headers, name, assetTypeId, parModelTypeId, modCommercialModelId, modelId):
    url = f"{config.BASE_URL_BE}/ModModel"
    payload = json.dumps({
        "name": name,
        "assetTypeId": assetTypeId,
        "parModelTypeId": parModelTypeId,
        "modCommercialModelId": modCommercialModelId, 
        "modelId": modelId
    })
    response = requests.put(url, headers=headers, data=payload)
    return response


# Eliminar un modelo por ID
def delete_model(headers, model_id):
    url = f"{config.BASE_URL_BE}/ModModel/{model_id}"
    response = requests.delete(url, headers=headers)
    return response


# Obtener todos los modelos y devolver los assetTypeIds
def get_asset_type_ids(headers):
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
