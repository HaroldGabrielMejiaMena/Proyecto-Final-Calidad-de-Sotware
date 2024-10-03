# Validar que el nombre actualizado coincide
def assert_name_matches(updated_data, expected_name):
    assert updated_data["name"] == expected_name, (
        f"Error: el nombre no se actualizó correctamente. Se esperaba {expected_name} pero se obtuvo {updated_data['name']}."
    )

# Validar que el countryId actualizado coincide
def assert_par_asset_category_id_matches(updated_data, expected_category_id):
    assert updated_data["parAssetCategoryId"] == expected_category_id, (
        f"Error: el parAssetCategoryId no se actualizó correctamente. Se esperaba {expected_category_id} pero se obtuvo {updated_data['parAssetCategoryId']}."
    )
    
# Validar que la respuesta es una lista de AssetTypes
def assert_asset_type_list(response_data):
    assert isinstance(response_data, list), f"Expected a list of AssetTypes but got {type(response_data)}."

# Validar que el ID del AssetType coincide
def assert_asset_type_id_matches(assettype_data, expected_assettype_id):
    assert assettype_data["assetTypeId"] == expected_assettype_id, (
        f"Error: expected AssetType ID {expected_assettype_id} but got {assettype_data['assetTypeId']}."
    )


# Validar que el campo 'name' existe en la respuesta del AssetType
def assert_asset_type_has_name(assettype_data):
    assert "name" in assettype_data, "Error: 'name' field is missing from AssetType response."

# Validar que el campo 'parAssetCategoryId' existe en la respuesta del AssetType
def assert_asset_type_has_par_asset_category_id(assettype_data):
    assert "parAssetCategoryId" in assettype_data, "Error: 'parAssetCategoryId' field is missing from AssetType response."
    
    
def assert_asset_type_data(assettype_data, expected_id, expected_name, expected_category_id):
    assert assettype_data["assetTypeId"] == expected_id, (
        f"Error: el ID del AssetType ({assettype_data['assetTypeId']}) no coincide con el esperado ({expected_id})."
    )
    assert assettype_data["name"] == expected_name, (
        f"Error: el nombre del AssetType ({assettype_data['name']}) no coincide con el esperado ({expected_name})."
    )
    assert assettype_data["parAssetCategoryId"] == expected_category_id, (
        f"Error: el 'parAssetCategoryId' ({assettype_data['parAssetCategoryId']}) no coincide con el esperado ({expected_category_id})."
    )
