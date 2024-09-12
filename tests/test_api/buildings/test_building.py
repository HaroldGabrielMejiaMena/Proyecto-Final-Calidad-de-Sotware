import pytest
from main.api.utils.buildings.building import post_create_building, get_building_by_id, delete_building, get_valid_country_and_city, put_update_building, get_building_by_name
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none
from tests.test_data.buildings.building_data import generate_building_data
from main.api.assertions.buildings.building_assertions import assert_building_exists, assert_building_matches_expected_data

"""@pytest.mark.api_automation
def test_create_building_without_setup(headers):
    response = post_create_building(headers,"Demo create", 22, "1231", 11)
    assert_get_status_code_200(response)"""
    
# Create a building 
@pytest.mark.api_automation
def test_create_building(headers, setup_create_building):
    building_id = setup_create_building
    assert building_id is not None, "El ID del building no debería ser None."

    # Obtener el building creado para validaciones
    building = get_building_by_id(headers, building_id)
    assert_get_status_code_200(building)
    

# Eliminar un building
@pytest.mark.api_automation   
def test_delete_building(headers, setup_create_building):
    building_id = setup_create_building
    delete_response = delete_building(headers, building_id)
    assert_get_status_code_200(delete_response)
    
    
# Prueba para actualizar un building
@pytest.mark.api_automation
def test_update_building(headers, setup_create_building):
    # Obtener el building_id desde el setup
    building_id = setup_create_building
    
    # Obtener datos de un country y city válidos
    country_id, city_id = get_valid_country_and_city(headers)
    
    # Generar datos aleatorios para el building
    updated_building_data = generate_building_data()
    
    # Realizar la actualización del building
    response = put_update_building(headers, updated_building_data["name"], country_id, updated_building_data["direction"], city_id, building_id)
    
    assert_get_status_code_200(response)
    
    # Verificar que el building se ha actualizado correctamente
    updated_building = get_building_by_name(headers, updated_building_data["name"])
    assert_building_exists(updated_building)
    
    # Validar que los campos actualizados sean correctos
    assert_building_matches_expected_data(updated_building, building_id, updated_building_data, city_id, country_id)