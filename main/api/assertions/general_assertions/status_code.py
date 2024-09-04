
        
def assert_get_status_code_200(response):
    assert response.status_code == 200


def assert_get_status_code_400(response):
    assert response.status_code == 400


def assert_get_status_code_401(response):
    assert response.status_code == 401


def assert_get_status_code_404(response):
    assert response.status_code == 404


def assert_get_status_code_405(response):
    assert response.status_code == 405
    
def assert_response_empty(response):    
    assert response.text == "", "Expected empty response but got some content."
 
   
