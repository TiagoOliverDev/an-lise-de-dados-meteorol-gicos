# import requests
# from bs4 import BeautifulSoup
import time
import pandas as pd
from ..utils.selenium_automation_tools import AutomationTools
from selenium.webdriver.common.by import By

auto_tools = AutomationTools()

class DataScrapingStations:

    @staticmethod
    def start():
        auto_tools.init_chrome_driver()
        auto_tools.go_to_page()
        data_stations = DataScrapingStations.get_tr_xpaths()

        general_data = []
        driver = auto_tools.get_driver()

        for station in data_stations:
            # print(xpath) 
            # auto_tools.click_xpath(xpath_btn=station['xpath'])
            auto_tools.click_xpath(xpath_btn='/html/body/table/tbody/tr[17]/td[1]/a')

            xpath_latitude = driver.find_element(By.XPATH, '/html/body/center/b/table/tbody/tr[2]/td[5]').text
            xpath_longitude = driver.find_element(By.XPATH, '/html/body/center/b/table/tbody/tr[2]/td[6]').text

            df_historical_data = DataScrapingStations.get_values_td_table()

            general_data.append({
                'ID externo da estacao': station['id_station'],
                'Nome da estacao': station['name_station'],
                'Latitude': xpath_latitude,
                'Longitude': xpath_longitude,
            })

            # auto_tools.go_to_page()
            time.sleep(2)
            break

        df_all_data = pd.DataFrame(general_data)

        return {'all_data': df_all_data, 'historical_data': df_historical_data}
    
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
    def get_value_columns_table():
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
    
    @staticmethod
    def get_values_td_table():
        driver = auto_tools.get_driver()
        # Primeiro, extraia o cabeçalho da tabela
        header_elements = driver.find_elements(By.XPATH, "/html/body/center/b/center/center/table/tbody/tr[1]/td")
        headers = [header.text for header in header_elements]

        # Agora, extraia os dados das linhas da tabela
        tr_elements = driver.find_elements(By.XPATH, "/html/body/center/b/center/center/table/tbody/tr[position()>1]")

        data_rows = []

        for tr_element in tr_elements:
            td_elements = tr_element.find_elements(By.TAG_NAME, "td")
            row_data = [td_element.text for td_element in td_elements]
            data_rows.append(row_data)

        df = pd.DataFrame(data_rows, columns=headers)

        return df
    

    
    # @staticmethod
    # def get_values_td_table():
    #     driver = auto_tools.get_driver()
    #     # Primeiro, extraia o cabeçalho da tabela
    #     header_elements = driver.find_elements(By.XPATH, "/html/body/center/b/center/center/table/tbody/tr[1]/td")
    #     headers = [header.text for header in header_elements]

    #     # Agora, extraia os dados das linhas da tabela
    #     tr_elements = driver.find_elements(By.XPATH, "/html/body/center/b/center/center/table/tbody/tr[position()>1]")

    #     data_rows = []

    #     for tr_element in tr_elements:
    #         td_elements = tr_element.find_elements(By.TAG_NAME, "td")
    #         row_data = [td_element.text for td_element in td_elements]
    #         data_rows.append(dict(zip(headers, row_data)))

    #     return data_rows
    

    
    # @staticmethod
    # def get_values_td_table():
    #     driver = auto_tools.get_driver()
    #     tr_elements = driver.find_elements(By.XPATH, "/html/body/center/b/center/center/table/tbody/tr")

    #     data_columns = []

    #     for tr_element in tr_elements:
    #         td_elements = tr_element.find_elements(By.TAG_NAME, "td")
    #         row_data = []

    #         for td_element in td_elements:
    #             data = td_element.text
    #             row_data.append({
    #                 'data': data,
    #             })

    #         data_columns.append(row_data)

    #     return data_columns
    

    
    
    

