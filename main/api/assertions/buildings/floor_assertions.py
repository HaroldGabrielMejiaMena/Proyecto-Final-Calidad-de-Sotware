

def assert_floor_updated_correctly(updated_floor_data, floor_data, floor_id, building_id):
    assert updated_floor_data["floorId"] == floor_id, f"Error: el ID del Floor no coincide. Esperado: {floor_id}, Actual: {updated_floor_data['floorId']}"
    assert updated_floor_data["name"] == floor_data["name"], f"Error: el nombre no coincide. Esperado: {floor_data['name']}, Actual: {updated_floor_data['name']}"
    assert updated_floor_data["parFloorTypeId"] == floor_data["parFloorTypeId"], f"Error: el parFloorTypeId no coincide. Esperado: {floor_data['parFloorTypeId']}, Actual: {updated_floor_data['parFloorTypeId']}"
    assert updated_floor_data["openingTime"] == floor_data["openingTime"], f"Error: el openingTime no coincide. Esperado: {floor_data['openingTime']}, Actual: {updated_floor_data['openingTime']}"
    assert updated_floor_data["closingTime"] == floor_data["closingTime"], f"Error: el closingTime no coincide. Esperado: {floor_data['closingTime']}, Actual: {updated_floor_data['closingTime']}"
    assert updated_floor_data["cleaningTime"] == floor_data["cleaningTime"], f"Error: el cleaningTime no coincide. Esperado: {floor_data['cleaningTime']}, Actual: {updated_floor_data['cleaningTime']}"
    assert updated_floor_data["buildingId"] == building_id, f"Error: el buildingId no coincide. Esperado: {building_id}, Actual: {updated_floor_data['buildingId']}"
