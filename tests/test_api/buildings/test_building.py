import pytest
import allure
from main.api.utils.buildings.building import post_create_building, get_building_by_id, delete_building, get_valid_country_and_city, put_update_building, get_building_by_name
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_get_status_code_500
from tests.test_data.buildings.building_data import generate_building_data
from main.api.assertions.buildings.building_assertions import assert_building_exists, assert_building_matches_expected_data
from main.api.utils.countries.country import post_create_a_country, delete_country, get_filtered_country, get_country_by_name
from main.api.utils.countries.country import post_create_a_country, delete_country 
from main.api.utils.countries.cities.city import post_create_a_city, delete_city, get_filtered_cities
from tests.test_data.countries.country_data import generate_country_data, generate_city_data


@allure.title("Verificar la creación de edificio básica")
@pytest.mark.api_automation
def test_create_building(headers, setup_create_building):
    
    building_id = setup_create_building
    building = get_building_by_id(headers, building_id)
    assert_get_status_code_200(building)


@allure.title("Verificar la creación de un edificio con datos vacíos")
@pytest.mark.api_automation
def test_create_building_without_fields(headers):
    
    response = post_create_building(headers,None, None, None, None)
    assert_get_status_code_400(response)   
    

@allure.title("Verificar la creación de edificio básica")
@pytest.mark.api_automation
def test_create_building_with_alphanumeric_characters(headers, setup_create_country, setup_create_city):
    
    country_id = setup_create_country
    city_id = setup_create_city
    building = post_create_building(headers,"AB12CD34", country_id, "1234 Elm Street", city_id )
    assert_get_status_code_200(building)


@allure.title("Validar la creación de un building con “Country” inhabilitado")
@pytest.mark.api_automation
def test_create_building_with_country_disabled(headers):
    country_data = generate_country_data()
    country = post_create_a_country(headers, country_data["name"], False)
    country = get_country_by_name(headers, country_data["name"])
    assert country is not None
    country_id = country["id"]
    
    city_data = generate_city_data(country_id)  

   
    city = post_create_a_city(headers, city_data["name"], city_data["available"], city_data["countryId"])
    
    assert_get_status_code_200(city)
    city_name = city_data["name"]
    
    filtered_response = get_filtered_cities(headers, name=city_name)
    
    city_id = filtered_response[0]["id"]
    building_data = generate_building_data()
    building = post_create_building(headers, building_data["name"], country_id, building_data["direction"], city_id)
    assert_get_status_code_400(building)
    


@allure.title("Verificar la eliminación de un edificio sin “Assets” asignados")
@pytest.mark.api_automation   
def test_delete_building(headers, setup_create_building):
    building_id = setup_create_building
    delete_response = delete_building(headers, building_id)
    assert_get_status_code_200(delete_response)
   
    
@allure.title("Verificar que se puedan editar los campos obligatorios del edificio")
@pytest.mark.api_automation
def test_update_building(headers, setup_create_building):
    building_id = setup_create_building
    
    country_id, city_id = get_valid_country_and_city(headers)
    
    updated_building_data = generate_building_data()
    
    response = put_update_building(headers, updated_building_data["name"], country_id, updated_building_data["direction"], city_id, building_id)
    
    assert_get_status_code_200(response)
    
    updated_building = get_building_by_name(headers, updated_building_data["name"])
    
    assert_building_exists(updated_building)
    assert_building_matches_expected_data(updated_building, building_id, updated_building_data, city_id, country_id)
     
    
@allure.title("Verificar que no se pueda guardar un edificio con campos obligatorios vacíos")
@pytest.mark.api_automation
def test_update_building_without_required_fields(headers, setup_create_building):
    building_id = setup_create_building
    
    country_id, city_id = get_valid_country_and_city(headers)
    
    response = put_update_building(headers, None, country_id, None, city_id, building_id)
    assert_get_status_code_400(response)
    
  

    
