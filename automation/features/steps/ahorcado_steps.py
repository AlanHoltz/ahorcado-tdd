from behave import given, when, then, step
import unittest
from automation.ahorcado_page import AhorcadoPage


@given('I open ahorcado page')
def i_am_on_the_homepage(context):
    print("I am on the homepage")
    # context.ahorcado_page = AhorcadoPage(context.driver)
    # context.driver.get('https://www.youtube.com/')
    
@when('ingreso la letra {letra}')
def ingreso_letra(context, letra):
    print("Ingreso letra")

@then('el juego me muestra {resultado}')
def juego_muestra(context, resultado):
    print("El juego me muestra resultado")