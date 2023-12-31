class Ahorcado:

    ESTADOS = {
        "DERROTA": -1,
        "EN_JUEGO": 0,
        "VICTORIA": 1,
    }

    def __init__ (self, palabra):
        self.palabra = palabra
        self.slots = self.inicializar_espacios()
        self.estado = self.ESTADOS["EN_JUEGO"]
        self.vidas = 6

    @classmethod
    def from_dict(cls,dict):
        instance = Ahorcado("RANDOM")
        instance.set_word(dict['palabra'])
        instance.set_slots(dict['slots'])
        instance.set_estado(dict['estado'])
        instance.set_vidas(dict['vidas'])
        return instance

    def set_word(self,word:str):
        self.palabra = word

    def set_slots(self,slots:str):
        self.slots = slots

    def set_estado(self,status: int):
        self.estado = status

    def set_vidas(self,hp: int):
        self.vidas = hp

    def loop_principal(self):
            while(self.estado == self.ESTADOS["EN_JUEGO"]):
                letra = input("Ingrese letra: ")
                self.arriesgar_letra(letra)
                self.actualizar_estado_juego()
                print(self.slots)
        # self.finaliza_juego()

    def letra_pertenece(self,letra):
        return letra in self.palabra
    
    def arriesgar_letra(self, letra):
        if self.letra_pertenece(letra):
            self.reemplazar_letra(letra)
        else:
            self.restar_vidas()

    def reemplazar_letra(self, letra):
        slots_sin_espacios = self.slots.replace(" ", "")
        for i,char in enumerate(self.palabra):
            if(char == letra):
                slots_sin_espacios = list(slots_sin_espacios)
                slots_sin_espacios[i] = letra
        slots_sin_espacios = " ".join(slots_sin_espacios)
        self.slots = slots_sin_espacios
    
    def partida_en_juego(self):
        return self.vidas > 0 and self.estado == self.ESTADOS["EN_JUEGO"] 
    
    def actualizar_estado_juego(self):
        if self.vidas == 0:
            self.estado = self.ESTADOS["DERROTA"]
        elif not "_" in self.slots: 
            self.estado = self.ESTADOS["VICTORIA"]

    def arriesgar_palabra(self, palabra):
        return palabra == self.palabra

    def inicializar_espacios(self):
        return ("_ " * len(self.palabra)).rstrip()
    
    def restar_vidas(self):
        self.vidas -= 1