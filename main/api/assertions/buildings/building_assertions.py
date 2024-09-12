

def assert_building_matches_expected_data(updated_building, building_id, updated_building_data, city_id, country_id):

    assert updated_building["buildingId"] == building_id, "Error: el ID del Building no coincide."
    assert updated_building["name"] == updated_building_data["name"], "Error: el nombre no coincide con el esperado."
    assert updated_building["cityId"] == city_id, "Error: el cityId no coincide."
    assert updated_building["countryId"] == country_id, "Error: el countryId no coincide con el esperado."


def assert_building_exists(updated_building):

    assert updated_building is not None, "Error: no se encontró el Building actualizado."