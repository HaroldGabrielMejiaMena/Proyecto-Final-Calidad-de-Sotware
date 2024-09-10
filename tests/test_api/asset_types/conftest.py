import pytest
from main.api.utils.asset_types.asset_types import post_create_asset_type, delete_asset_type, get_asset_type_by_name
from tests.test_data.asset_type.asset_type_data import generate_asset_type_data


# Setup para crear un AssetType
@pytest.fixture(scope="function")
def setup_create_assettype(headers, request):
    # Generar datos del AssetType utilizando Faker
    assettype_data = generate_asset_type_data()
    
    # Crear el AssetType
    response = post_create_asset_type(headers, assettype_data["name"], assettype_data["parAssetCategoryId"])
    
    # Verificar si la creación fue exitosa
    assert response.status_code == 200 or response.status_code == 201, f"Error al crear el AssetType: {response.status_code} - {response.text}"
    
    # Obtener el ID filtrando por nombre
    filtered_response = get_asset_type_by_name(headers, assettype_data["name"])
    
    # Verificamos si obtenemos el ID
    assert filtered_response is not None, f"No se encontró el AssetType con el nombre: {assettype_data['name']}"
    
    assettype_id = filtered_response["assetTypeId"]
    
    # Teardown: Eliminar el AssetType después de la prueba
    def teardown():
        delete_asset_type(headers, assettype_id)
    
    request.addfinalizer(teardown)
    
    return assettype_id
