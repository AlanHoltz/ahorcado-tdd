class Ahorcado:
    def __init__ (self, palabra):
        self.palabra = palabra
        self.estado = self.inicializar_espacios()
        self.vidas = 6

    def letra_pertenece(self,letra):
        return letra in self.palabra
    
    def arriesgar_letra(self, letra):
        if self.letra_pertenece(letra):
            nuevo_estado = self.estado.replace(" ", "")
            for i,char in enumerate(self.palabra):
                if(char == letra):
                    nuevo_estado = list(nuevo_estado)
                    nuevo_estado[i] = letra
            nuevo_estado = " ".join(nuevo_estado)
            
            self.estado = nuevo_estado
        else:
            self.restar_vidas()

    def arriesgar_palabra(self, palabra):
        return palabra == self.palabra

    def inicializar_espacios(self):
        return ("_ " * len(self.palabra)).rstrip()
    
    # def actualizar_estado(self, letra):
    
    # def juego_perdido(self):
    
    def restar_vidas(self):
        self.vidas -= 1