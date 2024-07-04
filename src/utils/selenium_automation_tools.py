from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import re
import json
import tempfile
import uuid

class AutomationTools:
    def __init__(self, download_dir: str = None, url: str = "http://sinda.crn.inpe.br/PCD/SITE/novo/site/cidades.php?uf=RN") -> None:
        """
        Initializes the AutomationTools object with a URL.
        
        Args:
        url (str): The default URL to be used for automation tasks.
        """
        self.download_dir = download_dir if download_dir else tempfile.gettempdir()
        self.driver = None
        self.url = url

    def init_chrome_driver(self) -> webdriver.Chrome:
        """
            Initializes and returns a Chrome WebDriver with specific options set to handle SSL and security warnings.
            
            Returns:
            webdriver.Chrome: The initialized Chrome WebDriver, or None if an error occurs.
        """
        try:    
            time.sleep(1)
            print('Initializing Chrome Driver...')  
            driver_path = ChromeDriverManager().install()   
            service = webdriver.chrome.service.Service(driver_path) 
            options = webdriver.ChromeOptions() 
         
            options.add_argument('--allow-running-insecure-content')
            options.add_argument('--disable-web-security')
            options.add_argument('--accept-insecure-certs')
            
            driver = webdriver.Chrome(service=service, options=options)
            self.driver = driver
            return driver       
        
        except Exception as e:      
            print(f"Error in init_chrome_driver(). Exception: {e}")      
            return None   

    def get_driver(self):
        return self.driver
        
    def get_path_in_download_dir(self) -> str:
        """
        Returns the most recently downloaded file in the download directory.
        
        Returns:
        str: The path of the most recently downloaded file.
        """
        try:
            files = os.listdir(self.download_dir)
            paths = [os.path.join(self.download_dir, basename) for basename in files]
            latest_file = max(paths, key=os.path.getctime)
            return latest_file
        except Exception as e:
            print(f"Error in get_latest_file_in_download_dir(). Exception: {e}")
            return None
        
    def rename_downloaded_file(self, original_path: str) -> str:
        """
            Renames the downloaded file to a UUID_relatorio_seguro.pdf format.
            
            Args:
            original_path (str): The original path of the downloaded file.
            
            Returns:
            str: The new path of the renamed file.
        """
        try:
            new_filename = f"{uuid.uuid4()}_relatorio_seguro.pdf"
            new_path = os.path.join(self.download_dir, new_filename)
            os.rename(original_path, new_path)
            return new_path
        except Exception as e:
            print(f"Error in rename_downloaded_file(). Exception: {e}")
            return None

    def go_to_page(self) -> None:
        """
        Navigates the driver to the URL set during initialization.
        
        Args:
        driver (webdriver.Chrome): The Chrome WebDriver.
        
        Returns:
        None: If an error occurs, prints the error and returns None.
        """
        try:
            time.sleep(1)
            self.driver.get(self.url)
        except Exception as e:
            print(f"Error in go_to_page(). Exception: {e}")

    def click_xpath(self, xpath_btn: str) -> None:
        """
        Clicks a button identified by an XPath.
        
        Args:
            xpath_btn (str): The XPath of the button to click.
            driver (webdriver.Chrome): The Chrome WebDriver.
        
        Returns:
            None: If an error occurs, prints the error and returns None.
        """
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_btn))
            )
            btn = self.driver.find_element(By.XPATH, xpath_btn)
            btn.click()
        except Exception as e:
            print(f"Error in click_xpath(). Exception: {e}")

    def upload_file_send_keys(self, css_selector: str, file_path: str, driver: webdriver.Chrome) -> None:
        """
        Uploads a file to an input field identified by a CSS selector.
        
        Args:
        css_selector (str): The CSS selector for the file input field.
        file_path (str): The path to the file to upload.
        driver (webdriver.Chrome): The Chrome WebDriver.
        
        Returns:
        None: If an error occurs, prints the error and returns None.
        """
        try:
            time.sleep(2)
            select_file = driver.find_element(By.CSS_SELECTOR, css_selector)
            select_file.send_keys(file_path)
        except Exception as e:
            print(f"Error in upload_file_send_keys(). Exception: {e}")

    def hover_over_element(self, driver: webdriver.Chrome, xpath: str) -> None:
        """
        Hovers the mouse over an element identified by XPath.
        
        Args:
        driver (webdriver.Chrome): The Chrome WebDriver.
        xpath (str): The XPath of the element to hover over.
        
        Returns:
        None: Performs the hover action.
        """
        element_to_hover_over = driver.find_element(By.XPATH, xpath)
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()

    def switch_to_window(self, driver: webdriver.Chrome, window_index: int) -> None:
        """
        Switches the WebDriver to another window/tab based on its index.
        
        Args:
        driver (webdriver.Chrome): The Chrome WebDriver.
        window_index (int): The index of the window/tab to switch to.
        
        Returns:
        None: If an error occurs, prints the error and returns None.
        """
        try:
            windows = driver.window_handles
            driver.switch_to.window(windows[window_index])
        except Exception as e:
            print(f"Error in switch_to_window(). Exception: {e}")

    def write_text(self, driver: webdriver.Chrome, xpath: str, text: str) -> None:
        """
        Writes text into an input field identified by XPath.

        Args:
        driver (webdriver.Chrome): The Chrome WebDriver.
        xpath (str): The XPath of the input field.
        text (str): The text to write into the input field.
        
        Returns:
        None: If an error occurs, prints the error and returns None.
        """
        try:
            time.sleep(1)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            input_field = driver.find_element(By.XPATH, xpath)
            input_field.clear()
            input_field.send_keys(text)
        except Exception as e:
            print(f"Error in write_text(). Exception: {e}")

    def extract_text(self, driver: webdriver.Chrome, xpath: str) -> str:
        """
        Extract text from input field identified by XPath.

        Args:
        driver (webdriver.Chrome): The Chrome WebDriver.
        xpath (str): The XPath of the input field.
        
        Returns:
        str: text extracted
        """
        try:
            time.sleep(1)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element = driver.find_element(By.XPATH, xpath)
            extracted_text = element.text

            return extracted_text
        except Exception as e:
            print(f"Error in extract_text(). Exception: {e}")
            return None
        
    def extract_num_from_text(self, driver: webdriver.Chrome, xpath: str) -> str:
        """             
        Extract num from return extract_text().

        Args:
        driver (webdriver.Chrome): The Chrome WebDriver.
        xpath (str): The XPath of the input field.
        
        Returns:
        str: num extracted
        """
        try:
            time.sleep(1)
            text = self.extract_text(driver=driver, xpath=xpath)
            
            match = re.search(r'Número do arquivo: (\d+)', text)
            if match:
                numero_arquivo = match.group(1)
                print(f'Número do arquivo: {numero_arquivo}')
            else:
                print('Número do arquivo não encontrado')

            return numero_arquivo
        except Exception as e:
            print(f"Error in extract_num_from_text(). Exception: {e}")
            return None
        
    def download_and_convert_to_pdf(self, driver: webdriver.Chrome):
        # Imprime a página como PDF
        driver.execute_script('window.print();')