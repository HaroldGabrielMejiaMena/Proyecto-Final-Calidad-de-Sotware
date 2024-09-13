import pytest
from main.api.utils.countries.country import post_create_a_country, delete_country, get_filtered_country, get_country_by_name
from tests.test_data.countries.country_data import generate_country_data, generate_department_data
from tests.test_data.countries.country_data import generate_city_data
from main.api.utils.countries.cities.city import post_create_a_city, delete_city, get_filtered_cities
from main.api.utils.countries.departaments.departaments import post_create_a_department, delete_department, get_filtered_departments

    
# Departaments    
@pytest.fixture(scope="function")
def setup_create_department(headers, setup_create_country):
    # Usar solo el country_id generado por el setup de país (el segundo valor de la tupla)
    country_id = setup_create_country
    #print("Este es el id", country_id)
    # Crear un departamento usando el country_id
    department_data = generate_department_data(country_id)
    response = post_create_a_department(headers, department_data["name"], department_data["countryId"])
    #print("Nombre del departemento ", department_data["name"])
    # Verificar si la creación del departamento fue exitosa
    if response.status_code != 200:
        raise Exception(f"Error al crear el departamento: {response.status_code} - {response.text}")

    # Filtrar y obtener el ID del departamento recién creado
    filtered_response = get_filtered_departments(headers, country_id)

    if not filtered_response:
        raise Exception(f"No se encontró el departamento con el nombre: {department_data['name']}")

    department_id = filtered_response[0]["departmentId"]
    yield department_id
    #print("Eliminando id: ", department_id)
    # Teardown para eliminar el departamento al final de la prueba
    delete_department(headers, department_id)



    


