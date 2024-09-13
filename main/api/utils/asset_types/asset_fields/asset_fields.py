import requests
import json
import config

# Crear un Asset Field
def post_create_asset_field(headers, is_required, asset_type_id, par_asset_field_id):
    url = f"{config.BASE_URL_BE}/AssetField"
    payload = json.dumps({
        "isRequired": is_required,
        "assetTypeId": asset_type_id,
        "parAssetFieldId": par_asset_field_id
    })
    response = requests.post(url, headers=headers, data=payload)
    return response

# Obtener un Asset Field filtrado por assetTypeId
def get_asset_fields_by_asset_type_id(headers, asset_type_id):
    url = f"{config.BASE_URL_BE}/AssetField/paginated?assetTypeId={asset_type_id}"
    response = requests.get(url, headers=headers)
    return response

# Obtener un AssetField por su ID.
def get_asset_field_by_id(headers, asset_field_id):
    url = f"{config.BASE_URL_BE}/AssetField/{asset_field_id}"
    response = requests.get(url, headers=headers)
    return response

# Actualizar un Asset Field
def put_update_asset_field(headers, asset_field_id, is_required, asset_type_id, par_asset_field_id):
    url = f"{config.BASE_URL_BE}/AssetField"
    payload = json.dumps({
        "isRequired": is_required,
        "assetTypeId": asset_type_id,
        "parAssetFieldId": par_asset_field_id,
        "assetFieldId": asset_field_id
    })
    response = requests.put(url, headers=headers, data=payload)
    return response

# Eliminar un Asset Field por ID
def delete_asset_field(headers, asset_field_id):
    url = f"{config.BASE_URL_BE}/AssetField/{asset_field_id}"
    response = requests.delete(url, headers=headers)
    return response
