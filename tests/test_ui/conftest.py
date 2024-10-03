import sys
import os
import logging
import pytest
import config
from core.ui.chrome_driver_manager_scd import ChromeDriverManager
from main.ui.pages.login_page import LoginPage

# Agregar el directorio raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")  # Cambiar a "function" para que cada prueba tenga su propio navegador
def driver(request):
    driver = ChromeDriverManager.get_chrome_driver()
    
    # Configurar la resolución de pantalla
    width = request.config.getoption("--width")
    height = request.config.getoption("--height")
    driver.set_window_size(width, height)
    
    yield driver
    driver.quit() 

def pytest_addoption(parser):
    parser.addoption("--width", action="store", default=1920, help="ancho de la ventana del navegador")
    parser.addoption("--height", action="store", default=1080, help="altura de la ventana del navegador")

def is_user_logged_in(driver):
    try:
        # Aquí defines un elemento que solo está visible si el usuario está logueado
        driver.find_element_by_xpath("//li//span[text()='Admin']")
        return True
    except:
        return False

@pytest.fixture(scope="session", autouse=True)
def login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to(config.BASE_URL)
    
    if not is_user_logged_in(driver):
        login_page.login(config.USERNAME, config.PASSWORD)
    else:
        logger.info("Usuario ya logueado. No es necesario hacer login de nuevo.")