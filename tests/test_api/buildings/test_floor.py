import pytest
from requests import Response
from main.api.utils.buildings import floor
from main.api.utils.buildings.floor import post_create_floor, put_update_floor, delete_floor, get_floor_by_id
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200
from tests.test_data.buildings.floor_data import generate_floor_data
from main.api.assertions.buildings.floor_assertions import assert_floor_updated_correctly

# Crear un floor
@pytest.mark.api_automation
def test_create_floor(headers, setup_create_floor):
    floor_id = setup_create_floor
    assert floor_id is not None, "El ID del building no debería ser None."

    # Obtener el building creado para validaciones
    floor = get_floor_by_id(headers, floor_id)
    assert_get_status_code_200(floor)
    

# Eliminar un floor
@pytest.mark.api_automation   
def test_delete_building(headers, setup_create_floor):
    floor_id = setup_create_floor
    delete_response = delete_floor(headers, floor_id)
    assert_get_status_code_200(delete_response)
    
    
# Prueba para actualizar un floor
@pytest.mark.api_automation
def test_update_building(headers, setup_create_floor):
    floor_id = setup_create_floor
    response = get_floor_by_id(headers, floor_id)
    building = response.json()
    building_id = building["buildingId"]
    floor_data = generate_floor_data(building_id) 
    response = put_update_floor(headers,floor_data["name"], floor_data["parFloorTypeId"], floor_data["openingTime"], floor_data["closingTime"], floor_data["cleaningTime"], building_id, floor_id)
    assert_get_status_code_200(response)
    updated_floor_response = get_floor_by_id(headers, floor_id)
    updated_floor_data = updated_floor_response.json()

    # Verificar si los cambios fueron aplicados correctamente
    assert_floor_updated_correctly(updated_floor_data, floor_data, floor_id, building_id)