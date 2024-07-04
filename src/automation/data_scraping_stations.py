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
        data_stations = DataScrapingStations.get_tr_xpaths()

        all_data = []
        driver = auto_tools.get_driver()

        for station in data_stations:
            # print(xpath)
            auto_tools.click_xpath(xpath_btn=station['xpath'])

            xpath_latitude = driver.find_element(By.XPATH, '/html/body/center/b/table/tbody/tr[2]/td[5]').text
            xpath_longitude = driver.find_element(By.XPATH, '/html/body/center/b/table/tbody/tr[2]/td[6]').text

            # tabela de dados históricos
            # /html/body/center/b/center/center/table/tbody/tr[1]/td[1]
            columns = DataScrapingStations.get_value_td_table()
            print('colunas: ', columns)

            all_data.append({
                'ID externo da estação': station['id_station'],
                'Nome da estação': station['name_station'],
                'Latitude': xpath_latitude,
                'Longitude': xpath_longitude,
            })

            # auto_tools.go_to_page()
            time.sleep(2)
            print(all_data)
            break
        # print(xpaths)
        return data_stations
    
    @staticmethod
    def get_tr_xpaths():
        driver = auto_tools.get_driver()
        tr_elements = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr")
        data_stations = []
        for index, element in enumerate(tr_elements, start=1):
            xpath = f"/html/body/table/tbody/tr[{index}]"
            if xpath != f"/html/body/table/tbody/tr[1]" and xpath != f"/html/body/table/tbody/tr[2]":
                xpath_id = f"{xpath}/td[1]/a"
                xpath_name = f"{xpath}/td[2]/a"
                xpath_id_element = driver.find_element(By.XPATH, xpath_id)
                xpath_name_element = driver.find_element(By.XPATH, xpath_name)
                id_station = xpath_id_element.text
                name_station = xpath_name_element.text
                data_stations.append({
                    'xpath': xpath+"/td[1]/a",
                    'id_station': id_station,
                    'name_station': name_station
                })
        return data_stations
    
    @staticmethod
    def get_value_td_table():
        driver = auto_tools.get_driver()
        tr_elements = driver.find_elements(By.XPATH, "/html/body/center/b/center/center/table/tbody/tr[1]/td")
        title_columns_stations = []
        for index, element in enumerate(tr_elements, start=1):
            xpath = f"/html/body/center/b/center/center/table/tbody/tr[1]/td[{index}]"
            collumns = driver.find_element(By.XPATH, xpath).text

            title_columns_stations.append({
                'columns': collumns,
            })
        return title_columns_stations
    
    
    

# /html/body/center/b/center/center/table/tbody/tr[2]

# /html/body/table/tbody/tr[{index}]/td[1]/a
# /html/body/table/tbody/tr[{index}]/td[2]/a



    # def fetch_weather_data(url: str):
    #     auto_tools.init_chrome_driver()
    #     auto_tools.go_to_page()
    #     auto_tools.click_xpath(xpath_btn='/html/body/table/tbody/tr[3]/td[1]/a')
    #     time.sleep(5)
