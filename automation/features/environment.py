from behave import *
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType

ahorcado_link = 'https://www.youtube.com/'
driver = webdriver.Chrome()

def before_all(context):
   print('Iniciando ATDD')
   driver = webdriver.Chrome()
   driver.get(ahorcado_link)
   
def after_all(context):
   print('Finalizando ATDD')
   driver.quit()
