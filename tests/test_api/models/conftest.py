import pytest
from tests.test_data.models.model_data import generate_commercial_model_data, generate_factory_model_data
from main.api.utils.models.models import post_create_comercial_model, get_model_by_name, delete_model, post_create_factory_model, get_model_by_id
from main.api.assertions.general_assertions.general_assertions import assert_get_status_code_200, assert_response_empty,assert_get_status_code_401,assert_get_status_code_400, assert_get_status_code_405, assert_id_not_none, assert_response_empty, assert_get_status_code_404, assert_get_status_code_500



# Setup para crear un comercial model con datos aleatorios
@pytest.fixture(scope="function")
def setup_commercial_model(headers, request, setup_create_asset_type):
    commercial_model_data = generate_commercial_model_data()
    asset_type_id = setup_create_asset_type  

    response = post_create_comercial_model(headers, commercial_model_data["name"], asset_type_id, commercial_model_data["parModelTypeId"], commercial_model_data["modCommercialModelId"])

    assert_get_status_code_200(response)
    filtered_response = get_model_by_name(headers, commercial_model_data["name"])
    assert filtered_response is not None, f"No se encontró el modelo comercial con el nombre: {commercial_model_data['name']}"
    
    commercial_model_id = filtered_response["modelId"]
    
    def teardown():
        delete_model(headers, commercial_model_id)
        
    request.addfinalizer(teardown)
    
    return commercial_model_id


# Setup para crear un factory model con datos aleatorios
@pytest.fixture(scope="function")
def setup_factory_model(headers, request, setup_commercial_model):
    commercial_model_id = setup_commercial_model
    model_response = get_model_by_id(headers, commercial_model_id)
    assert model_response.status_code == 200, f"Error al obtener el comercial model: {model_response.status_code} - {model_response.text}"
    model_data = model_response.json()
    asset_type_id = model_data.get("assetTypeId")
    assert asset_type_id is not None, "No se pudo obtener el assetTypeId del modelo comercial"
    
    factory_model_data = generate_factory_model_data(commercial_model_id)
    response = post_create_factory_model(headers, factory_model_data["name"], asset_type_id, factory_model_data["parModelTypeId"], factory_model_data["modCommercialModelId"])
    assert_get_status_code_200(response)
    
    filtered_response = get_model_by_name(headers, factory_model_data["name"])
    assert filtered_response is not None, f"No se encontró el modelo de fábrica con el nombre: {factory_model_data['name']}"
    
    factory_model_id = filtered_response["modelId"]
    def teardown():
        delete_model(headers, factory_model_id)
        
    request.addfinalizer(teardown)
    
    return factory_model_id