class Ahorcado:
    def __init__ (self):
        self.palabra = self.generar_palabra()

    def generar_palabra(self):
        return "palabra"

    def arriesgar_letra(self, letra):
        return letra in self.palabra

    def arriesgar_palabra(self, palabra):
        return palabra == self.palabra

    def mostrar_espacios(self):
        return ("_ " * len(self.palabra)).rstrip()