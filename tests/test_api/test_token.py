import pytest
from main.api.get_token import get_token


#@pytest.mark.api_automation
def test_obtener_token():
    # Llamar a la función para obtener el token
    token = get_token()

    # Aserciones para verificar el resultado
    assert token is not None, "El token de acceso no debe ser None"
    assert isinstance(token, str), "El token de acceso debe ser una cadena de texto"
    assert len(token) > 0, "El token de acceso no debe estar vacío"
    assert "Bearer" not in token, "El token de acceso no debe incluir la palabra 'Bearer'"