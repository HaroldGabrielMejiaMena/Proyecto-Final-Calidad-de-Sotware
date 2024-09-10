def assert_get_status_code_200(response):
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def assert_get_status_code_400(response):
    assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}. Response: {response.text}"

def assert_get_status_code_401(response):
    assert response.status_code == 401, f"Expected status code 401 but got {response.status_code}. Response: {response.text}"

def assert_get_status_code_404(response):
    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}. Response: {response.text}"

def assert_get_status_code_405(response):
    assert response.status_code == 405, f"Expected status code 405 but got {response.status_code}. Response: {response.text}"
    
def assert_get_status_code_500(response):
    assert response.status_code == 500, f"Expected status code 500 but got {response.status_code}. Response: {response.text}"

def assert_response_empty(response):    
    assert response.text == "", f"Expected empty response but got: {response.text}"

def assert_id_not_none(id):
    assert id is not None, "Expected ID not to be None, but it was None."


