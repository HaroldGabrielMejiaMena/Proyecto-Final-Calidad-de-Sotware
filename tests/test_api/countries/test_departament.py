import pytest
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_get_status_code_500
from tests.test_data.countries.country_data import generate_city_data, generate_department_data
from main.api.utils.countries.cities.city import get_city_by_id, post_create_a_city, put_update_city, delete_city
import allure
from main.api.utils.countries.departaments.departaments import post_create_a_department, delete_department, get_filtered_departments, get_department_by_id, put_update_department, get_departament_by_name
from main.api.assertions.countries.departament_asstertions import assert_department_id_matches, assert_department_has_required_fields, assert_department_country_id_updated, assert_department_name_updated


@allure.title("Verificar la creación de un departamento con un nombre válido")
@pytest.mark.api_automation
def test_create_department(headers, setup_create_department):
    department_id = setup_create_department
    assert_id_not_none(department_id)

    response = get_department_by_id(headers, department_id)
    assert_get_status_code_200(response)

    department_data = response.json()

    assert_department_id_matches(department_data,department_id)

    assert_department_has_required_fields(department_data)


@allure.title("Verificar que no se permita crear un departamento con un nombre duplicado") 
@pytest.mark.api_automation
def test_create_departament_with_duplicate_name(headers, setup_create_department):
    departament_id = setup_create_department
    departament = get_department_by_id(headers, departament_id)
    departament_response = departament.json()
    departament_name = departament_response["name"]
    country_id = departament_response["countryId"]
    response = post_create_a_department(headers, departament_name, country_id)
    assert_get_status_code_500(response)
 
  
@allure.title("Verificar que no se permita crear un departamento sin nombre")   
@pytest.mark.api_automation
def test_create_departament_without_name(headers, setup_create_country):
    country_id = setup_create_country
    response = post_create_a_department(headers, "", country_id)
    assert_get_status_code_400(response)  
    
    
@allure.title("Verificar que no se permita editar un departamento con un nombre duplicado") 
@pytest.mark.api_automation
def test_update_departament_with_duplicate_name(headers, setup_create_department):
    second_departament = "SecondDepartament"
    departament_id = setup_create_department
    departament_response =  get_department_by_id(headers, departament_id)
    departament = departament_response.json()
    departament_name = departament["name"]
    country_id = departament["countryId"]
    
    post_create_departament_response = post_create_a_department(headers, second_departament, country_id)
    assert_get_status_code_200(post_create_departament_response) 
    
    second_city_response = get_departament_by_name(headers, second_departament, country_id)
    assert second_city_response, "No se encontró el segundo country recién creado."
    second_departament_id = second_city_response["departmentId"]
    
    update_response = put_update_department(headers, second_departament_id, departament_name, country_id)
    assert_get_status_code_500(update_response)  
    response = delete_department(headers, second_departament_id)
    assert_get_status_code_200(response)        
     
@allure.title("Verificar la edición del nombre de un departamento") 
@pytest.mark.api_automation
def test_update_department(headers, setup_create_country, setup_create_department):
    department_id = setup_create_department
    assert_id_not_none(department_id)
    country_id = setup_create_country  

    updated_name = "Updated Department Name"
    response = put_update_department(headers, department_id, updated_name, country_id)
    assert_get_status_code_200(response)

    updated_response = get_department_by_id(headers, department_id)
    assert_get_status_code_200(updated_response)
    updated_data = updated_response.json()
    
    assert_department_id_matches(updated_data, department_id)
    assert_department_has_required_fields(updated_data)
    assert_department_name_updated(updated_data, updated_name)
    assert_department_country_id_updated(updated_data, country_id)

@allure.title("Verificar la eliminación exitosa de un departamento sin dependencias")    
@pytest.mark.api_automation
def test_delete_department(headers, setup_create_department):
    department_id = setup_create_department
    assert_id_not_none(department_id)

    delete_response = delete_department(headers, department_id)
    assert_get_status_code_200(delete_response)

    get_response = get_department_by_id(headers, department_id)
    assert_get_status_code_500(get_response)




