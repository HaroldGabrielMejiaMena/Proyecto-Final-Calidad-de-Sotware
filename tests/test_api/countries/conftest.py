import pytest
from main.api.utils.countries.country import post_create_a_country, delete_country, get_filtered_country, get_country_by_name
from tests.test_data.countries.country_data import generate_country_data, generate_department_data
from tests.test_data.countries.country_data import generate_city_data
from main.api.utils.countries.cities.city import post_create_a_city, delete_city, get_filtered_cities
from main.api.utils.countries.departaments.departaments import post_create_a_department, delete_department, get_filtered_departments

    
# Departaments    
@pytest.fixture(scope="function")
def setup_create_department(headers, setup_create_country):
    country_id = setup_create_country

    department_data = generate_department_data(country_id)
    response = post_create_a_department(headers, department_data["name"], department_data["countryId"])

    if response.status_code != 200:
        raise Exception(f"Error al crear el departamento: {response.status_code} - {response.text}")

    filtered_response = get_filtered_departments(headers, country_id)

    if not filtered_response:
        raise Exception(f"No se encontró el departamento con el nombre: {department_data['name']}")

    department_id = filtered_response[0]["departmentId"]
    yield department_id

    delete_department(headers, department_id)



    


