import pytest
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_get_status_code_500
from tests.test_data.countries.country_data import generate_city_data, generate_department_data
from main.api.utils.countries.cities.city import get_city_by_id, post_create_a_city, put_update_city, delete_city
import requests
import config
from main.api.utils.countries.departaments.departaments import post_create_a_department, delete_department, get_filtered_departments, get_department_by_id, put_update_department
from main.api.assertions.countries.departament_asstertions import assert_department_id_matches, assert_department_has_required_fields, assert_department_country_id_updated, assert_department_name_updated


"""@pytest.mark.api_automation
def test_create_department(headers, setup_get_id_country):
    # Usar el ID del país generado en el setup
    country_id = setup_get_id_country
    department_data = generate_department_data(country_id)

    # Crear el departamento
    response = post_create_a_department(headers, department_data["name"], country_id)
    
    # Verificar el código de estado y que no haya contenido en la respuesta
    assert response.status_code == 200
    assert response.text == """

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

 
 
@pytest.mark.api_automation
def test_update_department(headers, setup_create_country, setup_create_department):
    # Verificamos que el ID del departamento no sea None
    department_id = setup_create_department
    assert_id_not_none(department_id)

    # Usamos el country_id del setup_create_country que se genera dinámicamente
    _, country_id = setup_create_country  # Obtener el country_id creado

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




