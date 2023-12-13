from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.driver.get("http://34.176.37.34/")
    time.sleep(1)
    
def after_scenario(context, scenario):
    context.driver.quit()