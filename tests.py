import unittest
from ahorcado import Ahorcado
class Test(unittest.TestCase):

    def test_arriesgar_letra_y_adivinar(self):
       ahorcado = Ahorcado()
       self.assertTrue(ahorcado.arriesgar_letra("b"))

    def test_arriesgar_letra_y_errar(self):
       ahorcado = Ahorcado()
       self.assertFalse(ahorcado.arriesgar_letra("e"))

    def test_arriesgar_palabra_y_adivinar(self):
       ahorcado = Ahorcado()
       self.assertTrue(ahorcado.arriesgar_palabra("palabra"))

    def test_arriesgar_palabra_y_errar(self):
       ahorcado = Ahorcado()
       self.assertFalse(ahorcado.arriesgar_palabra("otrapalabra"))

    def test_mostrar_espacios(self):
       ahorcado = Ahorcado()
       self.assertEqual(ahorcado.mostrar_espacios(), "_ _ _ _ _ _ _")

if __name__ == '__main__':
    unittest.main()