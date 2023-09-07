from processing.constant import driver_path
import processing.scrape.Bank_thianland.constant as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Bank_thailand_scraper(webdriver.Chrome):
    def __init__(self, path, driver_path=driver_path, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": path
        })
        super(Bank_thailand_scraper, self).__init__(executable_path=driver_path, options=chrome_options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def get_csv(self):
        gotit = self.find_element(By.XPATH, '//*[@id="container-55222efc2a"]/div/div[3]/div/div/div/div/table/tbody/tr[3]/td[3]/button/span')
        gotit.click()

        currency_element = self.find_element(By.XPATH, '//*[@id="container-b9454cb2b1"]/div/div[2]/bot-statistics/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/button[2]/i')
        currency_element.click()

        download_csv = self.find_element(By.XPATH, '//*[@id="container-b9454cb2b1"]/div/div[2]/bot-statistics/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[1]/button')
        download_csv.click()
