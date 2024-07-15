import time
import pandas as pd
import selenium.common.exceptions as selexcept
import selenium.common.exceptions as NoSuchElementException
from ..utils.selenium_automation_tools import AutomationTools
from selenium.webdriver.common.by import By
from ..repositories.station_repository import StationRepository
from ..repositories.historic_data_repository import HistoricDataRepository
from ..db.database import SessionLocal



class DataScrapingStations:
    def __init__(self):
        self.auto_tools = AutomationTools()
        self.db = SessionLocal()
        self.station_repo = StationRepository(self.db)
        self.historic_data_repo = HistoricDataRepository(self.db)
            
    def start(self):
        self.auto_tools.init_chrome_driver()
        self.auto_tools.go_to_page()
        xpaths_stations = self.get_stations_xpaths()

        general_data = []
        driver = self.auto_tools.get_driver()

        for station in xpaths_stations:
            self.auto_tools.click_xpath(xpath_btn=station['xpath']) 
            # self.auto_tools.click_xpath(xpath_btn='/html/body/table/tbody/tr[5]/td[1]/a')
            # self.auto_tools.click_xpath(xpath_btn='/html/body/table/tbody/tr[17]/td[1]/a')

            name_station = driver.find_element(By.XPATH, '/html/body/center/b/table/tbody/tr[2]/td[2]').text
            xpath_latitude = driver.find_element(By.XPATH, '/html/body/center/b/table/tbody/tr[2]/td[5]').text
            xpath_longitude = driver.find_element(By.XPATH, '/html/body/center/b/table/tbody/tr[2]/td[6]').text

            if not name_station or not xpath_latitude or not xpath_longitude:
                self.auto_tools.go_to_page()
                time.sleep(2)
                continue

            df_historical_data = self.get_values_td_table()

            if isinstance(df_historical_data, dict) and 'Erro' in df_historical_data:
                print('Sem dados históricos:', df_historical_data['Erro'])
                self.auto_tools.go_to_page()
                time.sleep(2)
                continue

            station_record = self.station_repo.create_station(
                name=name_station,
                latitude=xpath_latitude,
                longitude=xpath_longitude
            )

            for index, row in df_historical_data.iterrows():
                for column in df_historical_data.columns:
                    value_data = row[column]
                    if value_data is not None: 
                        historic_data_result = self.historic_data_repo.create_historic_data(
                            name_data=column,
                            value_data=value_data,
                            station_id=station_record.id
                        )
                        if isinstance(historic_data_result, str):
                            print(historic_data_result)  

                
            general_data.append({
                'ID externo da estacao': station['id_station'],
                'Nome da estacao': name_station,
                'Latitude': xpath_latitude,
                'Longitude': xpath_longitude,
            })

            self.auto_tools.go_to_page()
            time.sleep(2)
            # break

        df_all_data = pd.DataFrame(general_data)

        return {'all_data': df_all_data, 'historical_data': df_historical_data}
    

    def get_stations_xpaths(self):
        driver = self.auto_tools.get_driver()
        tr_elements = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr")
        data_stations = []
        for index, element in enumerate(tr_elements, start=1):
            xpath = f"/html/body/table/tbody/tr[{index}]"
            if xpath != f"/html/body/table/tbody/tr[1]" and xpath != f"/html/body/table/tbody/tr[2]":
                xpath_id = f"{xpath}/td[1]/a"
                xpath_id_element = driver.find_element(By.XPATH, xpath_id)
                id_station = xpath_id_element.text
                data_stations.append({
                    'xpath': xpath+"/td[1]/a",
                    'id_station': id_station,
                })
        return data_stations
    

    def get_values_td_table(self):
        driver = self.auto_tools.get_driver()

        header_elements = driver.find_elements(By.XPATH, "/html/body/center/b/center/center/table/tbody/tr[1]/td")
        
        if not header_elements:
            return {'Erro': 'Cabeçalho da tabela está vazio.'}
        
        headers = [header.text for header in header_elements]

        tr_elements_validator = driver.find_elements(By.XPATH, "/html/body/center/b/center/center/table/tbody/tr[position()>1]/td")

        if not tr_elements_validator:
            return {'Erro': 'Linhas da tabela estão vazias.'}
        
        tr_elements = driver.find_elements(By.XPATH, "/html/body/center/b/center/center/table/tbody/tr[position()>1]")
        data_rows = []

        for tr_element in tr_elements:
            td_elements = tr_element.find_elements(By.TAG_NAME, "td")
            row_data = [td_element.text for td_element in td_elements]
            data_rows.append(row_data)
        
        if not data_rows:
            return {'Erro': 'Nenhum dado encontrado nas linhas da tabela.'}

        df = pd.DataFrame(data_rows, columns=headers)

        return df
    



    
    
    

