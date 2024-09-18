import pytest
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_get_status_code_500
from tests.test_data.countries.country_data import generate_city_data
from main.api.utils.countries.cities.city import get_city_by_id, post_create_a_city, put_update_city, delete_city, get_city_by_name
from main.api.utils.countries.country import get_first_country_id
import requests
import config


# Creacion de un city    
@pytest.mark.api_automation
def test_create_city_with_name(headers, setup_create_city):
    city_id = setup_create_city
    assert_id_not_none(city_id)
    # Validar que la ciudad fue creada correctamente
    response = get_city_by_id(headers, city_id)
    assert_get_status_code_200(response)


# Validación de Nombre Duplicado
@pytest.mark.api_automation
def test_create_city_with_duplicate_name(headers, setup_create_city):
    city_id = setup_create_city
    city = get_city_by_id(headers, city_id)
    city_response = city.json()
    city_name = city_response["name"]
    country_id = city_response["countryId"]
    response = post_create_a_city(headers, city_name, True, country_id)
    assert_get_status_code_500(response)


# Prueba para validar la respuesta al intentar crear un city sin nombre    
@pytest.mark.api_automation
def test_create_city_without_name(headers, setup_create_country):
    country_id = setup_create_country
    # Enviar solicitud de creación de country sin nombre
    response = post_create_a_city(headers, "", True, country_id)
    assert_get_status_code_400(response)


# Prueba para validar que no se pueda actualizar un city a un nombre ya existente
@pytest.mark.api_automation
def test_update_country_with_duplicate_name(headers, setup_create_city):
    second_country = "SecondCountry"
    city_id = setup_create_city
    
    # Filtrar el city creado para obtener su nombre
    city_response = get_city_by_id(headers, city_id)
    city = city_response.json()
    city_name = city["name"]
    country_id = city["countryId"]
    
    # Crear un segundo city con un nombre diferente
    post_create_city_response = post_create_a_city(headers, second_country, True, country_id)
    assert_get_status_code_200(post_create_city_response) 
    
    # Filtrar el segundo city por nombre para obtener su ID
    second_city_response = get_city_by_name(headers, second_country)
    assert second_city_response, "No se encontró el segundo country recién creado."
    second_city_id = second_city_response["id"]
    
    # Intentar actualizar el segundo city con el nombre del primer city 
    update_response = put_update_city(headers, second_city_id, city_name, True, country_id)
    assert_get_status_code_500(update_response)  
    response = delete_city(headers, second_city_id)
    assert_get_status_code_200(response)   
    
     
# Actualizar un city
@pytest.mark.api_automation
def test_update_city(headers, setup_create_city, setup_create_country):
    # Obtener el ID del city creado
    city_id = setup_create_city  # Recibe el city_id directamente
    assert_id_not_none(city_id)

    updated_name = "UpdatedCity"
    updated_available = False

    # Usa el country_id obtenido de la fixture setup_get_id_country
    country_id = setup_create_country

    # Actualizar el city
    response = put_update_city(headers, city_id, updated_name, updated_available, country_id)
    assert_get_status_code_200(response)

# Prueba para eliminar un country 
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
    country_id = setup_create_country
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
    country_id = setup_create_country
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