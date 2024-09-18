import pytest
import allure
from main.api.utils.buildings.floor import post_create_floor, put_update_floor, delete_floor, get_floor_by_id
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_get_status_code_400
from tests.test_data.buildings.floor_data import generate_floor_data
from main.api.assertions.buildings.floor_assertions import assert_floor_updated_correctly


@allure.title("Verificar la creación exitosa de un piso con todos los campos válidos")
@pytest.mark.api_automation
def test_create_floor(headers, setup_create_floor):
    floor_id = setup_create_floor
    assert floor_id is not None, "El ID del building no debería ser None."

    # Obtener el building creado para validaciones
    floor = get_floor_by_id(headers, floor_id)
    assert_get_status_code_200(floor)

@allure.title("Validar que no se puede crear un piso con campos obligatorios vacíos")
@pytest.mark.api_automation
def test_create_floor_without_requiered_fields(headers, setup_create_building):
    building_id = setup_create_building
    response = post_create_floor(headers, None, None, None, None, None, building_id )

    assert_get_status_code_400(response)
  

@allure.title("Validar que el sistema no permita guardar un piso si el horario de apertura es mayor o igual al horario de cierre")
@pytest.mark.api_automation
def test_create_floor_with_opening_time_greater_than_closing_time(headers, setup_create_building):
    building_id = setup_create_building
    floor_data = generate_floor_data(building_id)
    response = post_create_floor(headers, floor_data["name"], floor_data["parFloorTypeId"], "12:00:00", "11:59:59", floor_data["cleaningTime"], building_id )
    assert_get_status_code_400(response)
  
    
@allure.title("Validar que el sistema no permita crear un piso diferente a spot o parking")
@pytest.mark.api_automation
def test_create_floor_with_diferent_type(headers, setup_create_building):
    building_id = setup_create_building
    floor_data = generate_floor_data(building_id)
    response = post_create_floor(headers, floor_data["name"], "1", floor_data["openingTime"], floor_data["closingTime"], floor_data["cleaningTime"], building_id )
    assert_get_status_code_400(response)
        


@allure.title("Verificar la eliminación de un piso con un motivo válido")
@pytest.mark.api_automation   
def test_delete_building(headers, setup_create_floor):
    floor_id = setup_create_floor
    delete_response = delete_floor(headers, floor_id)
    assert_get_status_code_200(delete_response)
    
    
@allure.title("Verificar la modificación y guardado de todos los campos obligatorios de piso")
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