# Aserciones para Asset Fields

def assert_asset_field_id_matches(asset_field_data, expected_asset_field_id):
    assert asset_field_data["assetFieldId"] == expected_asset_field_id, (
        f"Error: expected Asset Field ID {expected_asset_field_id} but got {asset_field_data['assetFieldId']}."
    )

def assert_asset_field_has_required_fields(asset_field_data):
    assert "isRequired" in asset_field_data, "Error: 'isRequired' field not found in Asset Field data."
    assert "assetTypeId" in asset_field_data, "Error: 'assetTypeId' field not found in Asset Field data."
    assert "parAssetFieldId" in asset_field_data, "Error: 'parAssetFieldId' field not found in Asset Field data."
