import pytest
from main.api.utils.buildings import floor
from tests.test_data.buildings.building_data import generate_building_data
from tests.test_data.buildings.floor_data import generate_floor_data
from main.api.utils.buildings.building import post_create_building, get_building_by_name, delete_building
from main.api.utils.buildings.floor import post_create_floor, put_update_floor, delete_floor, get_floor_by_name


@pytest.fixture(scope="function")
def setup_create_building(headers, setup_create_country, setup_create_city, request):

    building_data = generate_building_data()
    
    country_id = setup_create_country
    
    city_id = setup_create_city

    response = post_create_building(headers, building_data["name"], country_id, building_data["direction"], city_id)

    assert response.status_code == 200 or response.status_code == 201, f"Error al crear el Building: {response.status_code} - {response.text}"

    building = get_building_by_name(headers, building_data["name"])
    assert building is not None, f"No se encontró el Building con el nombre {building_data['name']}."

    building_id = building["buildingId"]

    def teardown():

        delete_building(headers, building_id)

    request.addfinalizer(teardown)

    return building_id


#Floors
@pytest.fixture(scope="function")
def setup_create_floor(headers, setup_create_building, request):
    building_id = setup_create_building
    
    floor_data = generate_floor_data(building_id)

    response = post_create_floor(headers, floor_data["name"], floor_data["parFloorTypeId"], floor_data["openingTime"], floor_data["closingTime"], floor_data["cleaningTime"], building_id )

    assert response.status_code == 200 or response.status_code == 201, f"Error al crear el Building: {response.status_code} - {response.text}"

    floor = get_floor_by_name(headers, floor_data["name"])
    assert floor is not None, f"No se encontró el Building con el nombre {floor_data['name']}."

    floor_id = floor["floorId"]

    def teardown():
        
        delete_floor(headers, floor_id)

    request.addfinalizer(teardown)

    return floor_id

