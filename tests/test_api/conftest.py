import pytest
from main.api.get_token import get_token
from main.api.utils.asset_types.asset_types import post_create_asset_type, delete_asset_type, get_asset_type_by_name
from tests.test_data.asset_type.asset_type_data import generate_asset_type_data
from main.api.utils.countries.cities.city import post_create_a_city, delete_city, get_filtered_cities
from tests.test_data.countries.country_data import generate_country_data, generate_city_data
from main.api.utils.countries.country import post_create_a_country, delete_country, get_filtered_country, get_country_by_name

@pytest.fixture(scope="session")
def no_token():
    return {}

@pytest.fixture(scope="session")
def invalid_token():
    token = "eyJhbGciOiJSUzI1NiIsImtpZ"
    return token

@pytest.fixture(scope="session")
def valid_token():
    token = get_token()
    return token


@pytest.fixture(scope="session")
def headers(valid_token):
    return {
        "Authorization": f"Bearer {valid_token}",
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'http://localhost:3033',
        'Referer': 'http://localhost:3033/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        }

# Setup para crear un AssetType
@pytest.fixture(scope="function")
def setup_create_asset_type(headers, request):
    assettype_data = generate_asset_type_data()
    
    response = post_create_asset_type(headers, assettype_data["name"], assettype_data["parAssetCategoryId"])
    
    assert response.status_code == 200, f"Error al crear el AssetType: {response.status_code} - {response.text}"
    
    filtered_response = get_asset_type_by_name(headers, assettype_data["name"])
    
    assert filtered_response is not None, f"No se encontró el AssetType con el nombre: {assettype_data['name']}"
    
    assettype_id = filtered_response["assetTypeId"]
    
    def teardown():
        delete_asset_type(headers, assettype_id)
    
    request.addfinalizer(teardown)
    
    return assettype_id


#Cities
@pytest.fixture(scope="function")
def setup_create_city(headers, setup_create_country):
    city_data = generate_city_data(setup_create_country)  

    response = post_create_a_city(headers, city_data["name"], city_data["available"], city_data["countryId"])

    if response.status_code == 401:
        raise Exception("Error de autenticación: El token no es válido o ha expirado")

    city_name = city_data["name"]
    filtered_response = get_filtered_cities(headers, name=city_name)  

    if not filtered_response:
        raise Exception(f"No se encontró la ciudad con el nombre: {city_name}")

    city_id = filtered_response[0]["id"]
    yield city_id
    delete_city(headers, city_id)
    

# Countries
@pytest.fixture(scope="function")
def setup_create_country(headers, request):
    country_data = generate_country_data()
    response = post_create_a_country(headers, country_data["name"], country_data["available"])
    assert response.status_code == 200 
    country = get_country_by_name(headers, country_data["name"])
    assert country is not None
    country_id = country["id"]
    def teardown():
        delete_country(headers, country_id) 
    request.addfinalizer(teardown)
    return country_id
