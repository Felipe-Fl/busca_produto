from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class SeleniumServices():   
    def __init__(self):
        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")  # Executa sem abrir janela
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
        self.by = By

    def start_driver(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)
        return self.driver

    def quit_driver(self):
        self.driver.quit()