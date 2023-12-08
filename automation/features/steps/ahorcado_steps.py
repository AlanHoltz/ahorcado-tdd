from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setUp(context):
    if len(context.driver.find_elements(By.XPATH, '//*[contains(@class, "modal_back_button")]')) > 0:
            context.driver.find_element(By.XPATH, '//*[contains(@class, "modal_back_button")]').click()
            boton_iniciar_juego = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[text()="Nuevo Juego"]')))
            boton_iniciar_juego.click()
    if len(context.driver.find_elements(By.XPATH, '//*[contains(@class, "leave_game_button")]')) > 0:
        context.driver.find_element(By.XPATH, '//*[contains(@class, "leave_game_button")]').click()
        boton_iniciar_juego = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[text()="Nuevo Juego"]')))
        boton_iniciar_juego.click()

@when(u'Inicio nuevo juego')
def step_impl(context):
    try:
        setUp(context)
    except:
        pass
    finally:
        boton_iniciar_juego = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[text()="Nuevo Juego"]')))
        boton_iniciar_juego.click()

@when(u'Salgo del juego')
def step_impl(context):
    boton_salir = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "leave_game_button")]'))
    )
    boton_salir.click()


@when('Ingreso la letra "{letra}"')
def step_impl(context, letra):
    boton_letra = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="key" and text()="%s"]' %letra))
    )
    boton_letra.click()
    WebDriverWait(context.driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="key used_key"][text()="%s"]' %letra))
    )


@then(u'Estoy en la página inicial')
def step_impl(context):
   titulo = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//h1'))
    )
   
   assert titulo.text == "Ahorcado"
   
@then(u'Se muestra pantalla de victoria')
def step_impl(context):
   titulo_modal = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//h1[@class="modal_title"]'))
    )
   
   assert titulo_modal.text == "HAS GANADO!"
   
@then(u'Se muestra pantalla de derrota')
def step_impl(context):
   titulo_modal = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//h1[@class="modal_title"]'))
    )
   
   assert titulo_modal.text == "HAS PERDIDO!"
   
@then(u'El numero de intentos es "{numero_intentos}"')
def step_impl(context, numero_intentos):
   cantidad_correcta_intentos = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//ul[@class="modal_status"]//li[3][text()="%s"]' %numero_intentos))
    )
   
   assert cantidad_correcta_intentos.is_displayed()
   
@then(u'La cantidad de vidas restantes es "{vidas_restantes}"')
def step_impl(context, vidas_restantes):
   cantidad_correcta_vidas = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//ul[@class="modal_status"]//li[4][text()="%s"]' %vidas_restantes))
    )
   assert cantidad_correcta_vidas.is_displayed()
   boton_volver = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "modal_back_button")]')))
   boton_volver.click()
   WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[text()="Nuevo Juego"]')))
