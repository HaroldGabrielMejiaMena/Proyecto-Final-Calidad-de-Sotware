import requests
import json
import config


def get_all_asset_types(headers):
    url = f"{config.BASE_URL_BE}/AssetType"
    response = requests.get(url, headers=headers)
    return response


def get_asset_type_by_name(headers, name):
    url = f"{config.BASE_URL_BE}/AssetType/paginated?Name={name}&Page=1&PageSize=1"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error al obtener AssetType por nombre: {response.status_code}")

    data = response.json()

    #print(f"Response JSON: {data}")

    if "data" in data:
        if data["data"]:
            return data["data"][0]  
    else:
        raise Exception("No se encontró la clave 'data' en la respuesta.")




def get_asset_type_by_id(headers, assettype_id):
    url = f"{config.BASE_URL_BE}/AssetType/{assettype_id}"
    response = requests.get(url, headers=headers)
    return response


def post_create_asset_type(headers, name, parAssetCategoryId):
    url = f"{config.BASE_URL_BE}/AssetType"
    payload = json.dumps({
        "name": name,
        "parAssetCategoryId": parAssetCategoryId
    })
    response = requests.post(url, headers=headers, data=payload)
    return response


def put_update_asset_type(headers, assettype_id, name, parAssetCategoryId):
    url = f"{config.BASE_URL_BE}/AssetType"
    payload = json.dumps({
        "assetTypeId": assettype_id, 
        "name": name,
        "parAssetCategoryId": parAssetCategoryId
    })
    response = requests.put(url, headers=headers, data=payload)
    return response



def delete_asset_type(headers, assettype_id):
    url = f"{config.BASE_URL_BE}/AssetType/{assettype_id}"
    response = requests.delete(url, headers=headers)
    return response
