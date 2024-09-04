import pytest
from core.ui.chrome_driver_manager_scd import ChromeDriverManager
from main.ui.pages.login_page import LoginPage
import config
from main.ui.pages.buildings_page import BuildingsPage
import time

@pytest.mark.ui_automation
def test_login(driver):
    # Verificar si el login fue exitoso comprobando el título de la página
    """titulo = driver.title
    print(f"Título de la página después del login: {titulo}")"""
    
    buildings_page = BuildingsPage(driver)
    
    time.sleep(1)  # Pausa temporal para asegurar que la página esté cargada
    
    buildings_page.click_buildings()
    
    time.sleep(1)  # Otra pausa antes de la siguiente acción
    
    buildings_page.click_add_row()  # Verifica que este método también tenga un selector correcto
    time.sleep(1)
