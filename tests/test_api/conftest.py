import pytest
from main.api.get_token import get_token
from tests.test_data.countries.country_data import generate_country_data
from main.api.utils.countries.country import post_create_a_country, delete_country, get_filtered_country
import config



@pytest.fixture(scope="session")
def no_token():
    return {}

@pytest.fixture(scope="session")
def invalid_token():
    token = "eyJhbGciOiJSUzI1NiIsImtpZ"
    return token

@pytest.fixture(scope="session")
def valid_token():
    token = config.token
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
    

