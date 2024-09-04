import pytest
from main.api.utils.countries.country import post_create_a_country, delete_country, get_filtered_country
from tests.test_data.countries.country_data import generate_country_data
from tests.test_data.countries.country_data import generate_city_data
from main.api.utils.countries.cities.city import post_create_a_city, delete_city, get_filtered_cities
# Countries
@pytest.fixture(scope="function")
def setup_create_country(headers, request):
  # Generar los datos del country utilizando Faker
    country_data = generate_country_data()
    country_name = country_data["name"]
    #print(f"Nombre del country generado: {country_name}")
    # Crear el country
    response = post_create_a_country(headers, country_name, country_data["available"])
    #print(f"Response status code al crear el country: {response.status_code}")
    #print(f"Response text al crear el country: {response.text}")
    # Filtrar los countries usando el nombre recién creado para obtener el ID correcto
    filtered_response = get_filtered_country(headers, name=country_name)
    #print(f"Response del filtro: {filtered_response}")
    if not filtered_response:
        raise Exception(f"No se encontró el country con el nombre: {country_name}")
    
    country_id = filtered_response[0]["id"]
    #print(f"ID del country creado: {country_id}")
    # Teardown: Eliminar el country después de la prueba
    def teardown():
        #print(f"Eliminando el country con ID: {country_id}")
        delete_country(headers, country_id)
    
    request.addfinalizer(teardown)
    
    return response, country_id

@pytest.fixture(scope="function")
def setup_get_id_country(headers, request):
    """
    Este setup crea un country, obtiene su ID y asegura que el country sea eliminado al final de la prueba.
    """
    # Generar los datos del country utilizando Faker
    country_data = generate_country_data()
    country_name = country_data["name"]
    #print(f"Nombre del country generado: {country_name}")

    # Crear el country
    response = post_create_a_country(headers, country_name, country_data["available"])
    #print(f"Response status code al crear el country: {response.status_code}")
    #print(f"Response text al crear el country: {response.text}")

    # Verificar si la solicitud de creación fue exitosa
    if response.status_code == 401:
        raise Exception("Error de autenticación: El token no es válido o ha expirado")

    # Filtrar los countries usando el nombre recién creado para obtener el ID correcto
    filtered_response = get_filtered_country(headers, name=country_name)
    #print(f"Response del filtro: {filtered_response}")

    if not filtered_response:
        raise Exception(f"No se encontró el country con el nombre: {country_name}")

    country_id = filtered_response[0]["id"]
    #print(f"ID del country creado: {country_id}")

    # Teardown: Eliminar el country después de la prueba
    def teardown():
        #print(f"Eliminando el country con ID: {country_id}")
        delete_country(headers, country_id)

    request.addfinalizer(teardown)

    return country_id

#Cities
@pytest.fixture(scope="function")
def setup_create_city(headers, setup_get_id_country):
    city_data = generate_city_data(setup_get_id_country)  # Aquí usamos el country_id que retorna setup_create_country

    # Crear la ciudad
    response = post_create_a_city(headers, city_data["name"], city_data["available"], city_data["countryId"])

    # Verificar si la solicitud de creación fue exitosa
    if response.status_code == 401:
        raise Exception("Error de autenticación: El token no es válido o ha expirado")

    # Ahora buscamos la ciudad recién creada filtrando por su nombre
    city_name = city_data["name"]
    filtered_response = get_filtered_cities(headers, name=city_name)  # Cambiamos a filtrar por ciudad

    if not filtered_response:
        raise Exception(f"No se encontró la ciudad con el nombre: {city_name}")

    city_id = filtered_response[0]["id"]
    yield city_id
    delete_city(headers, city_id)  