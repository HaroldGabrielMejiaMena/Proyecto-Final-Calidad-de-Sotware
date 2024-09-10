


def assert_models_has_required_fields(model_data):
    assert "modelId" in model_data, "Error: 'modelId' field not found in Asset Field data."
    assert "name" in model_data, "Error: 'name' field not found in Asset Field data."
    assert "parModelTypeId" in model_data, "Error: 'parModelTypeId' field not found in Asset Field data."
    assert "parModelType" in model_data, "Error: 'parModelType' field not found in Asset Field data."
    assert "modCommercialModelId" in model_data, "Error: 'modCommercialModelId' field not found in Asset Field data."
    assert "modCommercialModel" in model_data, "Error: 'modCommercialModel' field not found in Asset Field data."
    assert "assetType" in model_data, "Error: 'assetType' field not found in Asset Field data."
    
    
def assert_models_id_matches(model_data, expected_model_id):
    assert model_data["modelId"] == expected_model_id, (
        f"Error: Expected brandId {expected_model_id} but got {model_data['modelId']}."
    )