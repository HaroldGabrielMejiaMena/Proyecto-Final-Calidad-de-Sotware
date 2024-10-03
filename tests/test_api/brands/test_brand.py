import pytest
import allure
from main.api.assertions.brands.brand_assertions import assert_brand_has_required_fields, assert_brand_id_matches, assert_brand_response_json
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_get_status_code_404, assert_response_empty
from tests.test_data.brands.brand_data import generate_brand_data
from main.api.utils.brands.brand import post_create_brand, delete_brand, get_brand_by_name, get_brand_by_id, put_update_brand
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_response_empty, assert_get_status_code_404, assert_get_status_code_500


@allure.title("Verificar la creación de una marca con nombre válido") 
@pytest.mark.api_automation
def test_create_brand(headers, setup_create_brand):
    brand_id = setup_create_brand
    assert_id_not_none(brand_id)
    response = get_brand_by_id(headers, brand_id)
    assert_get_status_code_200(response)
    brand_data = response.json()
    assert_brand_has_required_fields(brand_data)
    assert_brand_id_matches(brand_data, brand_id)
  
    
@allure.title("Verificar que no se permita crear una marca con datos vacíos") 
@pytest.mark.api_automation
def test_create_brand_without_fields(headers):
    response = post_create_brand(headers, None)
    assert_get_status_code_400(response)


@allure.title("Verificar la edición del nombre de la marca") 
@pytest.mark.api_automation
def test_update_brand(headers, setup_create_brand):
    brand_data = generate_brand_data()
    brand_id = setup_create_brand  
    response = put_update_brand(headers, brand_id,brand_data["name"])
    assert_get_status_code_200(response)
    assert_response_empty(response)


@allure.title("Verificar que no se permita editar una marca con el nombre vacío") 
@pytest.mark.api_automation
def test_update_brand_without_name(headers, setup_create_brand):
    brand_id = setup_create_brand  
    response = put_update_brand(headers, brand_id, None)
    assert_get_status_code_400(response)


@allure.title("Verificar la eliminación exitosa de una marca sin dependencias") 
@pytest.mark.api_automation
def test_delete_brand(headers, setup_create_brand):
    brand_id = setup_create_brand  
    response = delete_brand(headers, brand_id)
    assert_get_status_code_200(response)
    assert_response_empty(response)