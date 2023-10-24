from behave import given, when, then
from ahorcado import Ahorcado

@given('el juego del ahorcado')
@when('arriesgo la letra "{letra}"')
@then('los espacios son "{espacios}"')