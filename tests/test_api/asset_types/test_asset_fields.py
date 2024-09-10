import pytest
from main.api.utils.asset_types.asset_fields.asset_fields import post_create_asset_field, get_asset_fields_by_asset_type_id, put_update_asset_field, delete_asset_field, get_asset_field_by_id
from main.api.assertions.asset_types.asset_fields.asset_fields_assertions import assert_asset_field_id_matches, assert_asset_field_has_required_fields
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_get_status_code_404, assert_response_empty
from tests.test_data.asset_type.asset_field_data import generate_asset_field_data
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_response_empty, assert_get_status_code_404, assert_get_status_code_500


@pytest.mark.api_automation
def test_create_asset_field(headers, setup_create_asset_field, setup_create_asset_type):
    asset_field_id = setup_create_asset_field
    assert_id_not_none(asset_field_id)
    
    # Obtener el AssetField creado
    response = get_asset_field_by_id(headers, asset_field_id)
    assert_get_status_code_200(response)

    # Validar los datos retornados
    asset_field_data = response.json()

    # Verificar si los campos esperados están presentes
    assert_asset_field_has_required_fields(asset_field_data)
    assert "assetFieldId" in asset_field_data, "El campo 'assetFieldId' no se encontró en la respuesta."

    # Verificar que el AssetField pertenece al AssetType correcto
    assert asset_field_data["assetTypeId"] == setup_create_asset_type, "El assetTypeId no coincide con el AssetType creado."
    
# Prueba para obtener Asset Fields por assetTypeId
@pytest.mark.api_automation
def test_get_asset_fields_by_asset_type_id(headers, setup_create_asset_type):
    asset_type_id = setup_create_asset_type
    response = get_asset_fields_by_asset_type_id(headers, asset_type_id)
    assert_get_status_code_200(response)
    asset_fields_data = response.json()["data"]
    assert isinstance(asset_fields_data, list), "Error: expected a list of Asset Fields."

# Prueba para actualizar un Asset Field
@pytest.mark.api_automation
def test_update_asset_field(headers, setup_create_asset_field, setup_create_asset_type):
    asset_field_data = generate_asset_field_data()
    asset_field_id = setup_create_asset_field  
    asset_type_id = setup_create_asset_type 
    
    # Realizar la actualización
    response = put_update_asset_field(headers, asset_field_id, asset_field_data["isRequired"], asset_type_id,  asset_field_data["parAssetFieldId"])
    assert_get_status_code_200(response)

# Prueba para eliminar un Asset Field
@pytest.mark.api_automation
def test_delete_asset_field(headers, setup_create_asset_field):
    asset_field_id = setup_create_asset_field  
    response = delete_asset_field(headers, asset_field_id)
    assert_get_status_code_200(response)
    assert_response_empty(response)
