import pytest
from main.api.utils.asset_types.asset_types import get_asset_type_by_id, get_all_asset_types, delete_asset_type, put_update_asset_type
from tests.test_data.asset_type.asset_type_data import generate_asset_type_data
from main.api.assertions.asset_types.asset_types_assertions import assert_name_matches, assert_par_asset_category_id_matches, assert_asset_type_list, assert_asset_type_id_matches, assert_asset_type_has_name, assert_asset_type_has_par_asset_category_id, assert_asset_type_data
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_response_empty, assert_get_status_code_404, assert_get_status_code_500


# Prueba para crear un AssetType
@pytest.mark.api_automation
def test_create_assettype(headers, setup_create_asset_type):
    assettype_id = setup_create_asset_type
    assert_id_not_none(assettype_id)
    # Validar que el AssetType fue creado correctamente
    response = get_asset_type_by_id(headers, assettype_id)
    assert_get_status_code_200(response)
    # Validar los datos retornados
    assettype_data = response.json()
    # Validar que el ID coincide
    assert_asset_type_id_matches(assettype_data, assettype_id)
    # Verificar si los campos esperados están presentes
    assert_asset_type_has_name(assettype_data)
    assert_asset_type_has_par_asset_category_id(assettype_data)

# Prueba para eliminar un AssetType
@pytest.mark.api_automation
def test_delete_assettype(headers, setup_create_asset_type):
    assettype_id = setup_create_asset_type

    # Eliminar el AssetType
    response = delete_asset_type(headers, assettype_id)
    assert_get_status_code_200(response)
    assert_response_empty(response)  # Verificar que la respuesta es vacía

    # Validar que el AssetType ya no existe
    response = get_asset_type_by_id(headers, assettype_id)
    assert_get_status_code_500(response)
    

# Prueba para obtener todos los AssetTypes
@pytest.mark.api_automation
def test_get_all_assettypes(headers):
    response = get_all_asset_types(headers)
    assert_get_status_code_200(response)

    # Verificar que se haya retornado una lista
    assettypes_data = response.json()
    assert_asset_type_list(assettypes_data)

# Prueba para actualizar un AssetType
@pytest.mark.api_automation
def test_update_assettype(headers, setup_create_asset_type):
    assettype_id = setup_create_asset_type
    updated_name = "string2"
    updated_parAssetCategoryId = 2

    # Realizar la actualización
    response = put_update_asset_type(headers, assettype_id, updated_name, updated_parAssetCategoryId)
    assert_get_status_code_200(response)

    # Validar que los cambios se realizaron correctamente obteniendo de nuevo el AssetType
    updated_data = get_asset_type_by_id(headers, assettype_id).json()
    assert_asset_type_data(updated_data, assettype_id, updated_name, updated_parAssetCategoryId)
