

def assert_department_id_matches(department_data, department_id):
    """Valida que el ID del departamento en la respuesta coincida con el esperado."""
    assert department_data["departmentId"] == department_id, (
        f"Error: el ID del departamento en la respuesta ({department_data['departmentId']}) no coincide con {department_id}."
    )

def assert_department_has_required_fields(department_data):
    """Verifica que los campos 'name' y 'countryId' estén presentes en la respuesta del departamento."""
    assert "name" in department_data, "Error: no se encontró el campo 'name' en la respuesta del departamento."
    assert "countryId" in department_data, "Error: no se encontró el campo 'countryId' en la respuesta del departamento."
    
    
def assert_department_name_updated(department_data, expected_name):
    """
    Valida que el nombre del departamento se haya actualizado correctamente.
    
    :param department_data: Datos del departamento obtenidos de la respuesta.
    :param expected_name: El nombre que se espera después de la actualización.
    """
    assert department_data["name"] == expected_name, (
        f"Error: el nombre no se actualizó correctamente. Se esperaba {expected_name} pero se obtuvo {department_data['name']}."
    )
    

def assert_department_country_id_updated(department_data, expected_country_id):
    """
    Valida que el `countryId` del departamento se haya actualizado correctamente.
    
    :param department_data: Datos del departamento obtenidos de la respuesta.
    :param expected_country_id: El `countryId` que se espera después de la actualización.
    """
    assert department_data["countryId"] == expected_country_id, (
        f"Error: el countryId no se actualizó correctamente. Se esperaba {expected_country_id} pero se obtuvo {department_data['countryId']}."
    )


