import pytest
from main.api.utils.asset_types.asset_types import post_create_asset_type, delete_asset_type, get_asset_type_by_name
from tests.test_data.asset_type.asset_type_data import generate_asset_type_data
from main.api.utils.asset_types.asset_fields.asset_fields import post_create_asset_field, delete_asset_field, get_asset_fields_by_asset_type_id
from tests.test_data.asset_type.asset_field_data import generate_asset_field_data

# Setup para crear un AssetField
@pytest.fixture(scope="function")
def setup_create_asset_field(headers, setup_create_asset_type, request):
    # Generar datos del AssetField utilizando Faker
    asset_field_data = generate_asset_field_data()

    # Obtener el assetTypeId del setup de AssetType
    asset_type_id = setup_create_asset_type

    # Crear el AssetField
    response = post_create_asset_field(headers, asset_field_data["isRequired"], asset_type_id, asset_field_data["parAssetFieldId"])
    assert response.status_code == 200 or response.status_code == 201, f"Error al crear el AssetField: {response.status_code} - {response.text}"

    # Filtrar para obtener el assetFieldId
    filtered_response = get_asset_fields_by_asset_type_id(headers, asset_type_id)
    assert filtered_response.status_code == 200, f"Error al filtrar AssetField: {filtered_response.status_code} - {filtered_response.text}"

    asset_fields_data = filtered_response.json()["data"]
    assert len(asset_fields_data) > 0, "No se encontraron AssetFields para el AssetType creado."

    asset_field_id = asset_fields_data[0]["assetFieldId"]
    # Teardown: Eliminar el AssetField después de la prueba
    def teardown():
        delete_asset_field(headers, asset_field_id)
    request.addfinalizer(teardown)
    
    return asset_field_id
