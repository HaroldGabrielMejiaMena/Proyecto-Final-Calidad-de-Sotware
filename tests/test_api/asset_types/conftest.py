import pytest
from main.api.utils.asset_types.asset_types import post_create_asset_type, delete_asset_type, get_asset_type_by_name
from tests.test_data.asset_type.asset_type_data import generate_asset_type_data
from main.api.utils.asset_types.asset_fields.asset_fields import post_create_asset_field, delete_asset_field, get_asset_fields_by_asset_type_id
from tests.test_data.asset_type.asset_field_data import generate_asset_field_data

# Setup para crear un AssetField
@pytest.fixture(scope="function")
def setup_create_asset_field(headers, setup_create_asset_type, request):
    asset_field_data = generate_asset_field_data()
    asset_type_id = setup_create_asset_type

    response = post_create_asset_field(headers, asset_field_data["isRequired"], asset_type_id, asset_field_data["parAssetFieldId"])
    assert response.status_code == 200, f"Error al crear el AssetField: {response.status_code} - {response.text}"
    filtered_response = get_asset_fields_by_asset_type_id(headers, asset_type_id)
    
    assert filtered_response.status_code == 200, f"Error al filtrar AssetField: {filtered_response.status_code} - {filtered_response.text}"

    asset_fields_data = filtered_response.json()["data"]
    assert len(asset_fields_data) > 0, "No se encontraron AssetFields para el AssetType creado."
    asset_field_id = asset_fields_data[0]["assetFieldId"]
    
    def teardown():
        delete_asset_field(headers, asset_field_id)
    request.addfinalizer(teardown)
    
    return asset_field_id
