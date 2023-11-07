from behave import given, when, then, step
import unittest
from automation.ahorcado_page import AhorcadoPage


@given('I open ahorcado page')
def i_am_on_the_homepage(context):
    assert True
    
@when('ingreso la letra {letra}')
def ingreso_letra(context, letra):
    assert True
    
@then('el juego me muestra {resultado}')
def juego_muestra(resultado):
    assert True
    
@then('el juego no muestra {resultado}')
def juego_no_muestra(resultado):
    assert False