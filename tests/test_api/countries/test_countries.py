import pytest
from main.api.utils.countries.country import post_create_a_country,put_update_country, delete_country, get_filtered_country
from main.api.assertions.general_assertions.status_code import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405
from tests.test_data.countries.country_data import generate_country_data
import requests
import config

"""@pytest.mark.api_automation
def test_create_country_randon(headers):
    country_data = generate_country_data()
    response = post_create_a_country(country_data["name"], country_data["available"], headers)
    assert_get_status_code_200(response)
    assert_response_empty(response)"""
 
# Crear un country    
@pytest.mark.api_automation
def test_create_country_with_name(setup_create_country):
    response, _ = setup_create_country
    assert_get_status_code_200(response)
    assert_response_empty(response)

# Actualizar un country
@pytest.mark.api_automation
def test_update_country(headers, setup_create_country):
    # Obtener el ID del country creado
    _, country_id = setup_create_country
    updated_name = "UpdatedCountry"
    updated_available = False
    
    # Actualizar el country
    response = put_update_country(headers, country_id, updated_name, updated_available)
    assert_get_status_code_200(response)

# Prueba para eliminar un country utilizando el ID obtenido del setup.
@pytest.mark.api_automation
def test_delete_country(headers, setup_get_id_country):

    # Obtener el ID del country creado
    country_id = setup_get_id_country
    response = delete_country(headers, country_id)
    assert_get_status_code_200(response)

# No crear un country con un token invalido
@pytest.mark.api_automation
def test_create_country_with_invalid_token(invalid_token):
    country_data = generate_country_data()
    headers = {
        "Authorization": f"Bearer {invalid_token}",
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = post_create_a_country(headers, country_data["name"], country_data["available"])
    assert_get_status_code_401(response)
    
# No crear un country son token
@pytest.mark.api_automation
def test_create_country_without_token(no_token):
    country_data = generate_country_data()
    headers = {
        "Authorization": f"Bearer {no_token}",
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = post_create_a_country(headers, country_data["name"], country_data["available"])
    assert_get_status_code_401(response)

# No se cree un country con un medoto get 
@pytest.mark.api_automation
def test_create_country_with_wrong_http_method(headers):
    response = requests.get(f"{config.BASE_URL_BE}/Country", headers=headers)
    print(f"Status code: {response.status_code}")
    assert_get_status_code_405(response)


