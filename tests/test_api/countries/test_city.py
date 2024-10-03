import pytest
import allure
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_get_status_code_500
from tests.test_data.countries.country_data import generate_city_data
from main.api.utils.countries.cities.city import get_city_by_id, post_create_a_city, put_update_city, delete_city, get_city_by_name
from main.api.utils.countries.country import get_first_country_id


@allure.title("Verificar la creación de un departamento con un nombre válido")   
@pytest.mark.api_automation
def test_create_city_with_name(headers, setup_create_city):
    city_id = setup_create_city
    assert_id_not_none(city_id)
    response = get_city_by_id(headers, city_id)
    assert_get_status_code_200(response)


@allure.title("Verificar que no se permita crear una ciudad con un nombre duplicado")  
@pytest.mark.api_automation
def test_create_city_with_duplicate_name(headers, setup_create_city):
    city_id = setup_create_city
    city = get_city_by_id(headers, city_id)
    city_response = city.json()
    city_name = city_response["name"]
    country_id = city_response["countryId"]
    response = post_create_a_city(headers, city_name, True, country_id)
    assert_get_status_code_500(response)

  
@allure.title("Verificar que no se permita crear una ciudad sin nombre")   
@pytest.mark.api_automation
def test_create_city_without_name(headers, setup_create_country):
    country_id = setup_create_country
    response = post_create_a_city(headers, "", True, country_id)
    assert_get_status_code_400(response)


@allure.title("Verificar que no se permita editar una ciudad con un nombre duplicado") 
@pytest.mark.api_automation
def test_update_country_with_duplicate_name(headers, setup_create_city):
    second_country = "SecondCountry"
    city_id = setup_create_city
    city_response = get_city_by_id(headers, city_id)
    
    city = city_response.json()
    city_name = city["name"]
    country_id = city["countryId"]
    
    post_create_city_response = post_create_a_city(headers, second_country, True, country_id)
    assert_get_status_code_200(post_create_city_response) 
    
    second_city_response = get_city_by_name(headers, second_country)
    assert second_city_response, "No se encontró el segundo country recién creado."
    second_city_id = second_city_response["id"]

    update_response = put_update_city(headers, second_city_id, city_name, True, country_id)
    assert_get_status_code_500(update_response)  
    response = delete_city(headers, second_city_id)
    assert_get_status_code_200(response)   
    
     
@allure.title("Verificar la edición del nombre de una ciudad") 
@pytest.mark.api_automation
def test_update_city(headers, setup_create_city, setup_create_country):
    city_id = setup_create_city 
    assert_id_not_none(city_id)

    updated_name = "UpdatedCity"
    updated_available = False

    country_id = setup_create_country
    response = put_update_city(headers, city_id, updated_name, updated_available, country_id)
    assert_get_status_code_200(response)


@allure.title("Verificar la eliminación exitosa de una ciudad sin dependencias") 
@pytest.mark.api_automation
def test_delete_city(headers, setup_create_city):
    city_id = setup_create_city
    assert_id_not_none(city_id)
    response = delete_city(headers, city_id)
    assert_get_status_code_200(response)

