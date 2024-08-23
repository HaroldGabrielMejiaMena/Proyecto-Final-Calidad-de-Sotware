import pytest
from core.ui.chrome_driver_manager_scd import ChromeDriverManager
from main.ui.pages.login_page import LoginPage
import config


def test_login(driver):
    
    # Verificar si el login fue exitoso comprobando el título de la página
    titulo = driver.title
    print(f"Título de la página después del login: {titulo}")
    
