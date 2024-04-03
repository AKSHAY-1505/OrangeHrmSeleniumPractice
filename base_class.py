from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class BaseClass:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_url(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()

    def get_by_name(self, field_name):
        ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, field_name)))
        return ele

    def get_by_xpath(self, xpath):
        ele =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return ele

    def log_out(self):
        profile_button = self.get_by_xpath("//li[@class = 'oxd-userdropdown']")
        profile_button.click()

        logout_button = self.get_by_xpath("//ul[@class = 'oxd-dropdown-menu']//a[text() = 'Logout']")
        logout_button.click()

