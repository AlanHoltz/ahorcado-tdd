from behave import *
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType

ahorcado_link = 'https://www.youtube.com/'

def before_all(context):
   print('Iniciando ATDD')
   context.driver = webdriver.Chrome()
   context.driver.get(ahorcado_link)
   
def after_all(context):
   print('Finalizando ATDD')
   context.driver.quit()
