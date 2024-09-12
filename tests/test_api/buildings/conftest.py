import pytest
from tests.test_data.buildings.building_data import generate_building_data
from main.api.utils.buildings.building import post_create_building, get_building_by_name, delete_building

@pytest.fixture(scope="function")
def setup_create_building(headers, setup_create_country, setup_create_city, request):
    # Generar datos aleatorios para el building
    building_data = generate_building_data()

    # Obtener los IDs de country y city desde los setups correspondientes
    country_id = setup_create_country
    city_id = setup_create_city

    # Crear el Building usando tu método
    response = post_create_building(headers, building_data["name"], country_id, building_data["direction"], city_id)

    # Verificar si la creación fue exitosa
    assert response.status_code == 200 or response.status_code == 201, f"Error al crear el Building: {response.status_code} - {response.text}"

    # Filtrar por nombre si el servidor no devuelve el buildingId directamente
    building = get_building_by_name(headers, building_data["name"])
    assert building is not None, f"No se encontró el Building con el nombre {building_data['name']}."

    building_id = building["buildingId"]

    # Teardown: Eliminar el building después de la prueba
    def teardown():

        delete_building(headers, building_id)

    request.addfinalizer(teardown)

    return building_id

