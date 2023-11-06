from behave import *
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType

ahorcado_link = 'https://www.youtube.com/'

def before_all(context):
   print('Iniciando ATDD')
   context.allure_report_dir = 'allure-reports'
   context.driver = webdriver.Chrome()
   context.driver.get(ahorcado_link)
   
def after_all(context):
   print('Finalizando ATDD')
   context.driver.quit()

@allure.step('Capturar pantalla')
def capture_screenshot(context, step_name):
    allure.attach(context.driver.get_screenshot_as_png(), name=step_name, attachment_type=AttachmentType.PNG)

def after_step(context, step):
    if step.status == "failed":
        capture_screenshot(context, "screenshot")
