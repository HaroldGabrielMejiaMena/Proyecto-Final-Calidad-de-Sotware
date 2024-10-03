import pytest
import allure
from main.api.utils.asset_types.asset_fields.asset_fields import post_create_asset_field, get_asset_fields_by_asset_type_id, put_update_asset_field, delete_asset_field, get_asset_field_by_id
from main.api.assertions.asset_types.asset_fields.asset_fields_assertions import assert_asset_field_id_matches, assert_asset_field_has_required_fields
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_get_status_code_404, assert_response_empty
from tests.test_data.asset_type.asset_field_data import generate_asset_field_data
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_response_empty, assert_get_status_code_404, assert_get_status_code_500


@allure.title("Verificar la creación de un activo de campo con todos los campos válidos.")
@pytest.mark.api_automation
def test_create_asset_field(headers, setup_create_asset_field, setup_create_asset_type):
    asset_field_id = setup_create_asset_field
    assert_id_not_none(asset_field_id)
    
    response = get_asset_field_by_id(headers, asset_field_id)
    assert_get_status_code_200(response)

    asset_field_data = response.json()
    assert_asset_field_has_required_fields(asset_field_data)
    assert "assetFieldId" in asset_field_data, "El campo 'assetFieldId' no se encontró en la respuesta."
    assert asset_field_data["assetTypeId"] == setup_create_asset_type, "El assetTypeId no coincide con el AssetType creado."
   
    
@allure.title("Verificar que no se cree de un activo de campo sin campos.")
@pytest.mark.api_automation
def test_create_asset_field_without_fields(headers, setup_create_asset_type):
    asset_type_id = setup_create_asset_type
    assert_id_not_none(asset_type_id)
    
    response = post_create_asset_field(headers, None, asset_type_id, None)
    assert_get_status_code_400(response)
  

@allure.title("Verificar que no se cree de un activo de campo con un tipo diferente a Serial Code, IMEI y ROM.")
@pytest.mark.api_automation
def test_create_asset_field_with_different_field(headers, setup_create_asset_type):
    asset_type_id = setup_create_asset_type
    assert_id_not_none(asset_type_id)
    
    response = post_create_asset_field(headers, True, asset_type_id, 20)
    assert_get_status_code_400(response)  


@allure.title("Verificar los activos de campo.")
@pytest.mark.api_automation
def test_get_asset_fields_by_asset_type_id(headers, setup_create_asset_type):
    asset_type_id = setup_create_asset_type
    response = get_asset_fields_by_asset_type_id(headers, asset_type_id)
    assert_get_status_code_200(response)
    asset_fields_data = response.json()["data"]
    assert isinstance(asset_fields_data, list), "Error: expected a list of Asset Fields."

  
@allure.title("Verificar la actualizacion de un activo de campo con todos los campos válidos.")
@pytest.mark.api_automation
def test_update_asset_field(headers, setup_create_asset_field, setup_create_asset_type):
    asset_field_data = generate_asset_field_data()
    asset_field_id = setup_create_asset_field  
    asset_type_id = setup_create_asset_type 
    response = put_update_asset_field(headers, asset_field_id, asset_field_data["isRequired"], asset_type_id,  asset_field_data["parAssetFieldId"])
    assert_get_status_code_200(response)


@allure.title("Verificar que no se actualize un activo de campo con campos vacios.")
@pytest.mark.api_automation
def test_update_asset_field_without_fields(headers, setup_create_asset_field, setup_create_asset_type):
    asset_field_id = setup_create_asset_field  
    asset_type_id = setup_create_asset_type 
    response = put_update_asset_field(headers, asset_field_id, None, asset_type_id,  None)
    assert_get_status_code_400(response)


@allure.title("Verificar la eliminacion de un activo de campo.")
@pytest.mark.api_automation
def test_delete_asset_field(headers, setup_create_asset_field):
    asset_field_id = setup_create_asset_field  
    response = delete_asset_field(headers, asset_field_id)
    assert_get_status_code_200(response)
    assert_response_empty(response)
