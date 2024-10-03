from selenium import webdriver

class ChromeDriverManager:
    @staticmethod
    def get_chrome_driver():
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        return driver
    
    
    