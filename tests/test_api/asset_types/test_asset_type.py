import pytest
import allure
from requests import Response
from main.api.utils.asset_types.asset_types import get_asset_type_by_id, get_all_asset_types, delete_asset_type, put_update_asset_type, post_create_asset_type
from tests.test_data.asset_type.asset_type_data import generate_asset_type_data
from main.api.assertions.asset_types.asset_types_assertions import assert_name_matches, assert_par_asset_category_id_matches, assert_asset_type_list, assert_asset_type_id_matches, assert_asset_type_has_name, assert_asset_type_has_par_asset_category_id, assert_asset_type_data
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_response_empty, assert_get_status_code_404, assert_get_status_code_500


@allure.title("Verificar la creación de un tipo de activo con todos los campos válidos.")
@pytest.mark.api_automation
def test_create_assettype(headers, setup_create_asset_type):
    assettype_id = setup_create_asset_type
    assert_id_not_none(assettype_id)
    
    response = get_asset_type_by_id(headers, assettype_id)
    assert_get_status_code_200(response)
    
    assettype_data = response.json()
    assert_asset_type_id_matches(assettype_data, assettype_id)
    assert_asset_type_has_name(assettype_data)
    assert_asset_type_has_par_asset_category_id(assettype_data)


@allure.title("Verificar que no se permita crear un tipo de activo sin datos.")
@pytest.mark.api_automation
def test_create_assettype_without_fields(headers):
    response = post_create_asset_type(headers,None, None)
    assert_get_status_code_400(response)
  

@allure.title("Verificar que no se permita editar un tipo de activo sin nombre.")
@pytest.mark.api_automation
def test_update_assettype_without_name(headers, setup_create_asset_type):
    assettype_id = setup_create_asset_type
    updated_parAssetCategoryId = 2
    response = put_update_asset_type(headers, assettype_id, None, updated_parAssetCategoryId)
    assert_get_status_code_400(response)

    
@allure.title("Verificar que no se permita crear un activo diferente a CPU y Mobile")
@pytest.mark.api_automation
def test_update_assettype_with_diferent_category(headers):
    response = post_create_asset_type(headers, "Diferent Category", "4")
    assert_get_status_code_400(response) 


@allure.title("Verificar la edición de un activo.")
@pytest.mark.api_automation
def test_update_assettype(headers, setup_create_asset_type):
    assettype_id = setup_create_asset_type
    updated_name = "string2"
    updated_parAssetCategoryId = 2
    response = put_update_asset_type(headers, assettype_id, updated_name, updated_parAssetCategoryId)
    assert_get_status_code_200(response)

    updated_data = get_asset_type_by_id(headers, assettype_id).json()
    assert_asset_type_data(updated_data, assettype_id, updated_name, updated_parAssetCategoryId)   
       

@allure.title("Verificar la eliminación exitosa de un tipo de activo sin dependencias")
@pytest.mark.api_automation
def test_delete_assettype(headers, setup_create_asset_type):
    assettype_id = setup_create_asset_type
    response = delete_asset_type(headers, assettype_id)
    assert_get_status_code_200(response)
    assert_response_empty(response)  
    
    response = get_asset_type_by_id(headers, assettype_id)
    assert_get_status_code_500(response)
    

@allure.title("Verificar los activos disponibles")
@pytest.mark.api_automation
def test_get_all_assettypes(headers):
    response = get_all_asset_types(headers)
    assert_get_status_code_200(response)

    assettypes_data = response.json()
    assert_asset_type_list(assettypes_data)


