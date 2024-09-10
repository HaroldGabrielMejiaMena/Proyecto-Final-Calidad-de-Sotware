import pytest
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none
from tests.test_data.countries.country_data import generate_city_data
from main.api.utils.countries.cities.city import get_city_by_id, post_create_a_city, put_update_city, delete_city
import requests
import config

"""@pytest.mark.api_automation
def test_create_country_randon(headers):
    country_data = generate_city_data(22)
    response = post_create_a_city(headers, country_data["name"], country_data["available"], country_data["countryId"])
    assert_get_status_code_200(response)
    assert_response_empty(response)"""
    
@pytest.mark.api_automation
def test_create_city_with_name(headers, setup_create_city):
    city_id = setup_create_city
    assert_id_not_none(city_id)
    # Validar que la ciudad fue creada correctamente
    response = get_city_by_id(headers, city_id)
    assert_get_status_code_200(response)



@pytest.mark.api_automation
def test_create_city(headers,setup_create_city):
    city_id = setup_create_city  # Recibe el city_id directamente
    assert_id_not_none(city_id)  # Asegura que la ciudad fue creada

    # Ahora validamos si la ciudad fue efectivamente creada
    response = get_city_by_id(headers, city_id)
    assert_get_status_code_200(response)  # Verifica que la respuesta sea 200

# Actualizar un city
@pytest.mark.api_automation
def test_update_city(headers, setup_create_city, setup_get_id_country):
    # Obtener el ID del city creado
    city_id = setup_create_city  # Recibe el city_id directamente
    assert_id_not_none(city_id)

    updated_name = "UpdatedCity"
    updated_available = False

    # Usa el country_id obtenido de la fixture setup_get_id_country
    country_id = setup_get_id_country

    # Actualizar el city
    response = put_update_city(headers, city_id, updated_name, updated_available, country_id)
    assert_get_status_code_200(response)

# Prueba para eliminar un country utilizando el ID obtenido del setup.
@pytest.mark.api_automation
def test_delete_city(headers, setup_create_city):
    # Obtener el ID del city creado
    city_id = setup_create_city
    assert_id_not_none(city_id)
    # Eliminar la ciudad creada
    response = delete_city(headers, city_id)
    assert_get_status_code_200(response)

# No crear un city con un token invalido
@pytest.mark.api_automation
def test_create_city_with_invalid_token(invalid_token, setup_create_country):
    # Usa el country_id generado en el setup
    _, country_id = setup_create_country
    country_data = generate_city_data(country_id)

    headers = {
        "Authorization": f"Bearer {invalid_token}",
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'http://localhost:3033',
        'Referer': 'http://localhost:3033/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }
    # Crear el city
    response = post_create_a_city(headers, country_data["name"], country_data["available"], country_id)
    assert_get_status_code_401(response)
   
# No crear un city son token
@pytest.mark.api_automation
def test_create_city_without_token(no_token, setup_create_country):
    # Usa el country_id generado en el setup
    _, country_id = setup_create_country
    country_data = generate_city_data(country_id)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'http://localhost:3033',
        'Referer': 'http://localhost:3033/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    # Crear el city
    response = post_create_a_city(headers, country_data["name"], country_data["available"], country_id)
    assert_get_status_code_401(response)

# No se cree un city con un metodo HTTP incorrecto
@pytest.mark.api_automation
def test_create_country_with_wrong_http_method(headers):
    response = requests.get(f"{config.BASE_URL_BE}/City", headers=headers)
    assert_get_status_code_405(response)