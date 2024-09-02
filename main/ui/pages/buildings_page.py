from core.ui.base_page import BasePage
from selenium.webdriver.common.by import By
import time
class BuildingsPage(BasePage):
    #BUILDINGS_LOCATOR = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/ul[1]/li[2]")
    BUILDINGS_LOCATOR = (By.CSS_SELECTOR, ".ant-menu-item-only-child:nth-child(2)")
    ADD_ROW_LOCATOR = (By.CSS_SELECTOR, ".ant-btn-default.common-button:nth-child(2) > span:nth-child(1)")
    DASHBOARD_LOCATOR = (By.CSS_SELECTOR, ".ant-menu-item-only-child:nth-child(1)")
    
    def click_buildings(self):
        time.sleep(1)
        self.click(self.BUILDINGS_LOCATOR)
    def click_add_row(self):
        time.sleep(1)
        self.click(self. ADD_ROW_LOCATOR)
        self.click(self.DASHBOARD_LOCATOR)
        time.sleep(1)