import pytest
from main.api.utils.brands.brand import post_create_brand, delete_brand, get_brand_by_name
from tests.test_data.brands.brand_data import generate_brand_data


# Setup para crear un brand
@pytest.fixture(scope="function")
def setup_create_brand(headers, request):
    # Generar datos del brand utilizando Faker
    brand_data = generate_brand_data()
    
    # Crear el brand
    response = post_create_brand(headers, brand_data["name"])
    
    # Verificar si la creación fue exitosa
    assert response.status_code == 200 or response.status_code == 201, f"Error al crear el AssetType: {response.status_code} - {response.text}"
    
    # Obtener el ID filtrando por nombre
    filtered_response = get_brand_by_name(headers, brand_data["name"])
    
    # Verificamos si obtenemos el ID
    assert filtered_response is not None, f"No se encontró el brand con el nombre: {brand_data['name']}"
    
    brand_id = filtered_response["brandId"]
    
    # Teardown: Eliminar el brand después de la prueba
    def teardown():
        delete_brand(headers, brand_id)
        
    request.addfinalizer(teardown)
    
    return brand_id
