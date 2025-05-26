import time
from loguru import logger
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

class WebDriverGridClient:
    # Trying to connect to Selenium Grid with a specified number of attempts
    def wait_for_grid(self, url, max_retries=10, delay=5):
        for i in range(max_retries):
            try:
                driver = webdriver.Remote(command_executor=url, options=webdriver.ChromeOptions())
                driver.quit()
                logger.info("Successfully connected to Selenium Grid")
                return True
            except WebDriverException as e:
                logger.exception(f"Attempt {i+1}/{max_retries} failed: {e}")
                time.sleep(delay)
        raise Exception("Failed to connect to Selenium Grid")

    def __init__(self, site_url):
        self.grid_url = 'http://chrome:4444/wd/hub'
        self.wait_for_grid(self.grid_url)

        # Current site configuration
        self.site_url = site_url

        # Setting browser launch options
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.chrome_options.add_argument("--window-size=1250,800")
        
        # We install options in the driver
        self.driver = webdriver.Remote(command_executor=self.grid_url, options=self.chrome_options)

    def main(self):
        self.driver.get(self.site_url)
 
client = WebDriverGridClient("https://google.com")
client.main()

time.sleep(300)