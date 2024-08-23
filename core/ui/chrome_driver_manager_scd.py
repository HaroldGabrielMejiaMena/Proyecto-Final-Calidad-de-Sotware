from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class ChromeDriverManager:
    @staticmethod
    def get_chrome_driver():
        
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        return driver