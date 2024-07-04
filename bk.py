# import requests
# from bs4 import BeautifulSoup
import time
from ..utils.selenium_automation_tools import AutomationTools
from selenium.webdriver.common.by import By

auto_tools = AutomationTools()

class DataScrapingStations:

    @staticmethod
    def start():
        auto_tools.init_chrome_driver()
        auto_tools.go_to_page()
        xpaths = DataScrapingStations.get_tr_xpaths()
        for xpath in xpaths:
            print(xpath)
            auto_tools.click_xpath(xpath_btn=xpath)
            time.sleep(5)
            break
        # print(xpaths)
        return xpaths
    
    @staticmethod
    def get_tr_xpaths():
        driver = auto_tools.get_driver()
        tr_elements = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr")
        xpaths = []
        for index, element in enumerate(tr_elements, start=1):
            xpath = f"/html/body/table/tbody/tr[{index}]"
            if xpath != f"/html/body/table/tbody/tr[1]" and xpath != f"/html/body/table/tbody/tr[2]":
                xpaths.append(xpath+"/td[1]/a")
        return xpaths
    
    
    
# /html/body/table/tbody/tr[{index}]/td[1]/a
# /html/body/table/tbody/tr[{index}]/td[2]/a



    # def fetch_weather_data(url: str):
    #     auto_tools.init_chrome_driver()
    #     auto_tools.go_to_page()
    #     auto_tools.click_xpath(xpath_btn='/html/body/table/tbody/tr[3]/td[1]/a')
    #     time.sleep(5)
