

def assert_brand_has_required_fields(brand_data):
    assert "brandId" in brand_data, "Error: 'brandId' field not found in Asset Field data."
    assert "name" in brand_data, "Error: 'name' field not found in Asset Field data."
    
    
def assert_brand_id_matches(brand_data, expected_brand_id):
    assert brand_data["brandId"] == expected_brand_id, (
        f"Error: Expected brandId {expected_brand_id} but got {brand_data['brandId']}."
    )

def assert_brand_response_json(brand_data):
    assert isinstance(brand_data, dict), "Error: expected a dictionary (JSON object)."