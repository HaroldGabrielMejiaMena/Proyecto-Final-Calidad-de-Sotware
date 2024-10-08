import pytest
import allure
from main.api.utils.countries.country import post_create_a_country,put_update_country, delete_country, get_filtered_country, get_country_by_id, get_all_countries, get_country_by_name 
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_get_status_code_500
from main.api.utils.countries.departaments import departaments
from tests.test_data.countries.country_data import generate_country_data
from main.api.utils.countries.cities.city import delete_city, post_create_a_city, get_city_by_name, get_filtered_cities
from main.api.utils.countries.departaments.departaments import post_create_a_department, delete_department, get_departament_by_name
from main.api.assertions.countries.departament_asstertions import assert_department_found
import requests
import config


@allure.title("Verificar la creación de un país con los campos válidos")     
@pytest.mark.api_automation
def test_create_country_with_name(headers, setup_create_country):
    country_id = setup_create_country
    response = get_country_by_id(headers, country_id)
    assert_get_status_code_200(response)


@allure.title("Verificar que no se permita crear un país con un nombre duplicado")   
@pytest.mark.api_automation
def test_create_country_with_duplicate_name(headers, setup_create_country):
    country_id = setup_create_country
    country = get_country_by_id(headers, country_id)
    country_response = country.json()
    country_name = country_response["name"]
    response = post_create_a_country(headers, country_name, True)
    assert_get_status_code_500(response)


@allure.title("Verificar que no se permita crear un país sin nombre")   
@pytest.mark.api_automation
def test_create_country_without_name(headers):
    response = post_create_a_country(headers, "", True)
    assert_get_status_code_400(response)    


@allure.title("Verificar la edición del nombre y estado de disponibilidad de un país")
@pytest.mark.api_automation
def test_update_country(headers, setup_create_country):
    country_id = setup_create_country
    updated_name = "UpdatedCountry"
    updated_available = False
    response = put_update_country(headers, country_id, updated_name, updated_available)
    assert_get_status_code_200(response)


@allure.title("Verificar que no se permita guardar un nombre de país duplicado")
@pytest.mark.api_automation
def test_update_country_with_duplicate_name(headers, setup_create_country):
    country_id = setup_create_country
    
    country_response = get_country_by_id(headers, country_id)
    country = country_response.json()
    country_name = country["name"]
    
    post_create_country_response = post_create_a_country(headers, "SecondCountry", True)
    assert_get_status_code_200(post_create_country_response) 
    
    second_country_response = get_country_by_name(headers, "SecondCountry")
    assert second_country_response, "No se encontró el segundo country recién creado."
    second_country_id = second_country_response["id"]
    
    update_response = put_update_country(headers, second_country_id, country_name, True)
    assert_get_status_code_500(update_response)  

    response = delete_country(headers, second_country_id)
    assert_get_status_code_200(response)
    

@allure.title("Verificar la eliminación exitosa de un país sin dependencias")
@pytest.mark.api_automation
def test_delete_country(headers, setup_create_country):
    country_id = setup_create_country
    response = delete_country(headers, country_id)
    assert_get_status_code_200(response)
    
        
@allure.title("Verificar que no se puede eliminar un country si tiene ciudades registradas")
@pytest.mark.api_automation
def test_delete_country_with_city(headers, setup_create_country):
    country_id = setup_create_country
    
    city_name = "city_test"
    city_response = post_create_a_city(headers, city_name, True, country_id)
    assert_get_status_code_200(city_response) 
    
    filtered_city_response = get_filtered_cities(headers, name=city_name)
    
    city_id = filtered_city_response[0]["id"]
    
    response_after_city = delete_country(headers, country_id)
    assert_get_status_code_500(response_after_city)  
    
    response_delete_city = delete_city(headers, city_id)
    assert_get_status_code_200(response_delete_city) 
    
    response_after_city_deletion = delete_country(headers, country_id)
    assert_get_status_code_200(response_after_city_deletion)  



@allure.title("Verificar que no se puede eliminar un country si tiene departamentos registrados")
@pytest.mark.api_automation
def test_delete_country_with_department(headers, setup_create_country):
    country_id = setup_create_country
    
    department_name = "department_test"
    department_response = post_create_a_department(headers, department_name, country_id)
    assert_get_status_code_200(department_response) 
    
    filtered_department_response = get_departament_by_name(headers, department_name, country_id)
    
    department_id = filtered_department_response["departmentId"]
    
    response_after_department = delete_country(headers, country_id)
    assert_get_status_code_500(response_after_department)  
    
    response_delete_department = delete_department(headers, department_id)
    assert_get_status_code_200(response_delete_department)  
    
    response_after_department_deletion = delete_country(headers, country_id)
    assert_get_status_code_200(response_after_department_deletion)    
    
    

@allure.title("Verificar los countries registrados")
@pytest.mark.api_automation
def test_get_all_countries(headers):
    response = get_all_countries(headers)
    assert_get_status_code_200(response) 
    countries_data = response.json()["data"]
    assert isinstance(countries_data, list), "Error: expected a list of countries."
    assert len(countries_data) > 0, "Error: no countries found."
    

@allure.title("Verificar que no se cree un country con un token invalido")
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
    
    
@allure.title("Verificar que no se cree un country sin token")
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


@allure.title("Verificar que no se cree un country con un medoto get")
@pytest.mark.api_automation
def test_create_country_with_wrong_http_method(headers):
    response = requests.get(f"{config.BASE_URL_BE}/Country", headers=headers)
    assert_get_status_code_405(response)


