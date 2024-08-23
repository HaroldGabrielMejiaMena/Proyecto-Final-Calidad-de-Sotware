import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

class ChromeDriverManager:
    @staticmethod

    def get_chrome_driver():
        # Construir la ruta al ChromeDriver
        current_dir = os.path.dirname(os.path.abspath(__file__))

        chromedriver_path = os.path.abspath(os.path.join(current_dir, "..", "..", "core", "ui", "drivers", "chromedriver.exe"))
        
        # Inicializar el ChromeDriver con la ruta local
        service = ChromeService(executable_path=chromedriver_path)
        return webdriver.Chrome(service=service)