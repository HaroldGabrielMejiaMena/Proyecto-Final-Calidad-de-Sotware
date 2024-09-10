import pytest
import random
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_response_empty, assert_get_status_code_404, assert_get_status_code_500
from main.api.utils.models.models import post_create_comercial_model, get_model_by_name, delete_model, post_create_factory_model, get_model_by_id, put_update_comercial_model, put_update_factory_model, get_asset_type_ids
from main.api.assertions.models.models_assertions import assert_models_has_required_fields, assert_models_id_matches


# Crear un modelo comercial
@pytest.mark.api_automation
def test_create_commercial_model(headers, setup_commercial_model):
    model_id = setup_commercial_model
    assert model_id is not None, "Model ID should not be None"
    response = get_model_by_id(headers, model_id)
    assert_get_status_code_200(response)
    # Validar los datos retornados
    model_data = response.json()

    # Verificar si los campos esperados están presentes
    assert_models_has_required_fields(model_data)
    assert_models_id_matches(model_data, model_id)
    

# Crear un modelo de fabrica
@pytest.mark.api_automation
def test_create_factory_model(headers, setup_factory_model):
    model_id = setup_factory_model
    assert model_id is not None, "Factory Model ID should not be None"
    response = get_model_by_id(headers, model_id)
    assert_get_status_code_200(response)
    # Validar los datos retornados
    model_data = response.json()

    # Verificar si los campos esperados están presentes
    assert_models_has_required_fields(model_data)
    assert_models_id_matches(model_data, model_id)


# Eliminar un comercial model
@pytest.mark.api_automation   
def test_delete_commercial_model(headers, setup_commercial_model):
    model_id = setup_commercial_model
    delete_response = delete_model(headers, model_id)
    assert_get_status_code_200(delete_response)

# Eliminar un comercial model    
@pytest.mark.api_automation  
def test_delete_factory_model(headers, setup_factory_model):
    commercial_model_id = setup_factory_model
    delete_response = delete_model(headers, commercial_model_id)
    assert_get_status_code_200(delete_response)


# Actualizar un modelo comercial
@pytest.mark.api_automation 
def test_update_commercial_model(headers, setup_commercial_model):
    model_id = setup_commercial_model
    
    # Obtener una lista de assetTypeIds
    asset_type_ids = get_asset_type_ids(headers)
    
    # Seleccionar un assetTypeId aleatorio
    asset_type_id = random.choice(asset_type_ids)
    
    # Realizar la actualización
    response = put_update_comercial_model(headers, "Updated Comercial Model", asset_type_id, 3, None, model_id)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"


# Actualizar un modelo de fabrica    
@pytest.mark.api_automation 
def test_update_factory_model(headers, setup_factory_model):
    model_id = setup_factory_model
    
    # Obtener una lista de assetTypeIds
    asset_type_ids = get_asset_type_ids(headers)
    
    # Seleccionar un assetTypeId aleatorio
    asset_type_id = random.choice(asset_type_ids)
    
    # Realizar la actualización
    response = put_update_factory_model(headers, "Updated Factory Model", asset_type_id, 4, None, model_id)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

