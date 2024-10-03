import pytest
import random
import allure
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_response_empty, assert_get_status_code_404, assert_get_status_code_500
from main.api.utils.models.models import post_create_comercial_model, get_model_by_name, delete_model, post_create_factory_model, get_model_by_id, put_update_comercial_model, put_update_factory_model, get_asset_type_ids
from main.api.assertions.models.models_assertions import assert_models_has_required_fields, assert_models_id_matches


@allure.title("Verificar la creación de un modelo comercial con todos los campos válidos.") 
@pytest.mark.api_automation
def test_create_commercial_model(headers, setup_commercial_model):
    model_id = setup_commercial_model
    response = get_model_by_id(headers, model_id)
    assert_get_status_code_200(response)
    
    model_data = response.json()
    assert_models_has_required_fields(model_data)
    assert_models_id_matches(model_data, model_id)


@allure.title("Verificar la creación de un modelo de fabrica con todos los campos válidos.") 
@pytest.mark.api_automation
def test_create_factory_model(headers, setup_factory_model):
    model_id = setup_factory_model
    response = get_model_by_id(headers, model_id)
    assert_get_status_code_200(response)
    model_data = response.json()
    assert_models_has_required_fields(model_data)
    assert_models_id_matches(model_data, model_id)
    

@allure.title("Verificar que no se permita crear un modelo comercial sin completar los campos obligatorios.") 
@pytest.mark.api_automation
def test_create_comercial_model_without_required_fields(headers, setup_create_asset_type):
    asset_type_id = setup_create_asset_type
    response = post_create_comercial_model(headers, None, asset_type_id, 3, None)
    assert_get_status_code_400(response)


@allure.title("Verificar que no se permita crear un modelo fabrica sin completar los campos obligatorios.") 
@pytest.mark.api_automation
def test_create_factory_model_without_required_fields(headers, setup_commercial_model):   
    commercial_model_id = setup_commercial_model
    model_response = get_model_by_id(headers, commercial_model_id)
    assert_get_status_code_200(model_response)
    model_data = model_response.json()
    asset_type_id = model_data.get("assetTypeId")
    response = post_create_factory_model(headers, None, asset_type_id, 4, commercial_model_id)
    assert_get_status_code_400(response)


@allure.title("Verificar que no se permita crear un modelo diferente a modelo comercial o modelo de fabrica") 
@pytest.mark.api_automation
def test_create_factory_model_with_different_type(headers, setup_create_asset_type):   
    asset_type_id = setup_create_asset_type
    response = post_create_comercial_model(headers, "test", asset_type_id, 20, None)
    assert_get_status_code_400(response)


@allure.title("Verificar la edición del tipo de modelo comercial.")
@pytest.mark.api_automation 
def test_update_commercial_model(headers, setup_commercial_model):
    model_id = setup_commercial_model
    asset_type_ids = get_asset_type_ids(headers)
    asset_type_id = random.choice(asset_type_ids)
    response = put_update_comercial_model(headers, "Updated Comercial Model", asset_type_id, 3, None, model_id)
    assert_get_status_code_200(response)


@allure.title("Verificar la edición del tipo de modelo de fabrica.")   
@pytest.mark.api_automation 
def test_update_factory_model(headers, setup_factory_model):
    model_id = setup_factory_model
    asset_type_ids = get_asset_type_ids(headers)
    asset_type_id = random.choice(asset_type_ids)
    response = put_update_factory_model(headers, "Updated Factory Model", asset_type_id, 4, None, model_id)
    assert_get_status_code_200(response)


@allure.title("Verificar que no permita editar un modelo comercial con el nombre vacío.")
@pytest.mark.api_automation 
def test_update_commercial_model_without_name(headers, setup_commercial_model):
    model_id = setup_commercial_model
    asset_type_ids = get_asset_type_ids(headers)
    asset_type_id = random.choice(asset_type_ids)
    response = put_update_comercial_model(headers, None, asset_type_id, 3, None, model_id)
    assert_get_status_code_400(response)


@allure.title("Verificar que no permita editar un modelo de fabrica con el nombre vacío.")   
@pytest.mark.api_automation 
def test_update_factory_model_without_name(headers, setup_factory_model):
    model_id = setup_factory_model
    asset_type_ids = get_asset_type_ids(headers)
    asset_type_id = random.choice(asset_type_ids)
    response = put_update_factory_model(headers, None, asset_type_id, 4, None, model_id)
    assert_get_status_code_400(response)    

 
@allure.title("Verificar la eliminación de un modelo comercial.")
@pytest.mark.api_automation   
def test_delete_commercial_model(headers, setup_commercial_model):
    model_id = setup_commercial_model
    delete_response = delete_model(headers, model_id)
    assert_get_status_code_200(delete_response)


@allure.title("Verificar la eliminación de un modelo de fabrica.")  
@pytest.mark.api_automation  
def test_delete_factory_model(headers, setup_factory_model):
    commercial_model_id = setup_factory_model
    delete_response = delete_model(headers, commercial_model_id)
    assert_get_status_code_200(delete_response)



