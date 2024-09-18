import pytest
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_get_status_code_500
from tests.test_data.countries.country_data import generate_city_data, generate_department_data
from main.api.utils.countries.cities.city import get_city_by_id, post_create_a_city, put_update_city, delete_city
import requests
import config
from main.api.utils.countries.departaments.departaments import post_create_a_department, delete_department, get_filtered_departments, get_department_by_id, put_update_department, get_departament_by_name
from main.api.assertions.countries.departament_asstertions import assert_department_id_matches, assert_department_has_required_fields, assert_department_country_id_updated, assert_department_name_updated


# Crear un departamento
@pytest.mark.api_automation
def test_create_department(headers, setup_create_department):
    # Verificamos que el ID del departamento no sea None
    department_id = setup_create_department
    assert_id_not_none(department_id)

    # Validar que el departamento fue creado correctamente
    response = get_department_by_id(headers, department_id)
    assert_get_status_code_200(response)

    # Validar los datos del departamento en la respuesta
    department_data = response.json()

    # Validar que el ID coincide
    assert_department_id_matches(department_data,department_id)

    # Verificar si los campos esperados están presentes
    assert_department_has_required_fields(department_data)


# Validación de Nombre Duplicado
@pytest.mark.api_automation
def test_create_departament_with_duplicate_name(headers, setup_create_department):
    departament_id = setup_create_department
    departament = get_department_by_id(headers, departament_id)
    departament_response = departament.json()
    departament_name = departament_response["name"]
    country_id = departament_response["countryId"]
    response = post_create_a_department(headers, departament_name, country_id)
    assert_get_status_code_500(response)
 
 
# Prueba para validar la respuesta al intentar crear un departamento sin nombre    
@pytest.mark.api_automation
def test_create_departament_without_name(headers, setup_create_country):
    country_id = setup_create_country
    # Enviar solicitud de creación de country sin nombre
    response = post_create_a_department(headers, "", country_id)
    assert_get_status_code_400(response)  
    
    
# Prueba para validar que no se pueda actualizar un departamento a un nombre ya existente
@pytest.mark.api_automation
def test_update_departament_with_duplicate_name(headers, setup_create_department):
    second_departament = "SecondDepartament"
    departament_id = setup_create_department
    
    # Filtrar el city creado para obtener su nombre
    departament_response =  get_department_by_id(headers, departament_id)
    departament = departament_response.json()
    departament_name = departament["name"]
    country_id = departament["countryId"]
    
    # Crear un segundo city con un nombre diferente
    post_create_departament_response = post_create_a_department(headers, second_departament, country_id)
    assert_get_status_code_200(post_create_departament_response) 
    
    # Filtrar el segundo city por nombre para obtener su ID
    second_city_response = get_departament_by_name(headers, second_departament, country_id)
    assert second_city_response, "No se encontró el segundo country recién creado."
    second_departament_id = second_city_response["departmentId"]
    
    # Intentar actualizar el segundo city con el nombre del primer city 
    update_response = put_update_department(headers, second_departament_id, departament_name, country_id)
    assert_get_status_code_500(update_response)  
    response = delete_department(headers, second_departament_id)
    assert_get_status_code_200(response)        
     
# Actualizar un departamento 
@pytest.mark.api_automation
def test_update_department(headers, setup_create_country, setup_create_department):
    # Verificamos que el ID del departamento no sea None
    department_id = setup_create_department
    assert_id_not_none(department_id)

    # Usamos el country_id del setup_create_country que se genera dinámicamente
    country_id = setup_create_country  # Obtener el country_id creado

    # Datos actualizados
    updated_name = "Updated Department Name"

    # Realizamos la actualización del departamento
    response = put_update_department(headers, department_id, updated_name, country_id)
    assert_get_status_code_200(response)

    # Obtener los datos del departamento actualizado
    updated_response = get_department_by_id(headers, department_id)
    assert_get_status_code_200(updated_response)

    # Validar los datos del departamento actualizado
    updated_data = updated_response.json()
    
    # Validar que el ID coincide
    assert_department_id_matches(updated_data, department_id)
    
    # Verificar si los campos esperados están presentes
    assert_department_has_required_fields(updated_data)

    # Validar que el nombre y el countryId se actualizaron correctamente
    assert_department_name_updated(updated_data, updated_name)
    assert_department_country_id_updated(updated_data, country_id)
   
# Eliminar un departamento
@pytest.mark.api_automation
def test_delete_department(headers, setup_create_department):
    # Verificamos que el ID del departamento no sea None
    department_id = setup_create_department
    assert_id_not_none(department_id)

    # Eliminar el departamento
    delete_response = delete_department(headers, department_id)
    assert_get_status_code_200(delete_response)

    # Intentar obtener el departamento eliminado para verificar que ya no existe
    get_response = get_department_by_id(headers, department_id)
    assert_get_status_code_500(get_response)




