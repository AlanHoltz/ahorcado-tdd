from selenium.webdriver.common.by import By

class AhorcadoPage:
    def __init__(self, driver):
        self.driver = driver
        self.espacios = (By.ID, 'espacios')
        self.boton_enviar = (By.ID, 'enviar')

    def ingresar_letra(self, username):
        pass

    def iniciar_juego(self, password):
        pass

    def get_texto_fin_de_juego(self):
        pass