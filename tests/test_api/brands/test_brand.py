import pytest
from main.api.assertions.brands.brand_assertions import assert_brand_has_required_fields, assert_brand_id_matches, assert_brand_response_json
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_get_status_code_404, assert_response_empty
from tests.test_data.brands.brand_data import generate_brand_data
from main.api.utils.brands.brand import post_create_brand, delete_brand, get_brand_by_name, get_brand_by_id, put_update_brand
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_response_empty, assert_get_status_code_404, assert_get_status_code_500

# Crear brand
@pytest.mark.api_automation
def test_create_brand_field(headers, setup_create_brand):
    brand_id = setup_create_brand
    assert_id_not_none(brand_id)
    
    # Obtener el AssetField creado
    response = get_brand_by_id(headers, brand_id)
    assert_get_status_code_200(response)

    # Validar los datos retornados
    brand_data = response.json()

    # Verificar si los campos esperados están presentes
    assert_brand_has_required_fields(brand_data)
    assert_brand_id_matches(brand_data, brand_id)
    
    
# Prueba para obtener brands por id
@pytest.mark.api_automation
def test_get_brands_by_brand_id(headers, setup_create_brand):
    brand_id = setup_create_brand
    response = get_brand_by_id(headers, brand_id)
    assert_get_status_code_200(response)
    # Obtener los datos del body de la respuesta como JSON
    brand_data = response.json() 

    # Validar que el tipo de dato sea un diccionario (JSON válido)
    assert_brand_response_json(brand_data)
    # Verificar si los campos esperados están presentes
    assert_brand_has_required_fields(brand_data)

    # Validar que el brandId coincide con el ID esperado
    assert_brand_id_matches(brand_data, brand_id)


# Prueba para actualizar un Brand
@pytest.mark.api_automation
def test_update_brand(headers, setup_create_brand):
    brand_data = generate_brand_data()
    brand_id = setup_create_brand  
    
    # Realizar la actualización
    response = put_update_brand(headers, brand_id,brand_data["name"])
    assert_get_status_code_200(response)
    assert_response_empty(response)

# Prueba para eliminar un Asset Field
@pytest.mark.api_automation
def test_delete_brand(headers, setup_create_brand):
    brand_id = setup_create_brand  
    response = delete_brand(headers, brand_id)
    assert_get_status_code_200(response)
    assert_response_empty(response)