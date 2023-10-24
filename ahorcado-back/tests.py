import unittest
from ahorcado import Ahorcado
class Test(unittest.TestCase):

# Comment test

   def test_arriesgar_letra_y_errar(self):
      ahorcado = Ahorcado("palabra")
      ahorcado.arriesgar_letra("e")
      self.assertEqual(ahorcado.slots, "_ _ _ _ _ _ _")
      
   def test_arriesgar_letra_unica_y_acertar(self):
      ahorcado = Ahorcado("palabra")
      ahorcado.arriesgar_letra("p")
      self.assertEqual(ahorcado.slots, "p _ _ _ _ _ _")
   
   def test_arriesgar_letra_multiple_y_acertar(self):
      ahorcado = Ahorcado("palabra")
      ahorcado.arriesgar_letra("a")
      self.assertEqual(ahorcado.slots, "_ a _ a _ _ a")

   def test_arriesgar_palabra_y_adivinar(self):
      ahorcado = Ahorcado("palabra")
      self.assertTrue(ahorcado.arriesgar_palabra("palabra"))

   def test_arriesgar_palabra_y_errar(self):
      ahorcado = Ahorcado("palabra")
      self.assertFalse(ahorcado.arriesgar_palabra("otrapalabra"))

   def test_inicializar_espacios(self):
      ahorcado = Ahorcado("palabra")
      self.assertEqual(ahorcado.inicializar_espacios(), "_ _ _ _ _ _ _")

   def test_actualizar_vidas(self):
      ahorcado = Ahorcado("palabra")
      vidas_actual = ahorcado.vidas
      ahorcado.restar_vidas()
      self.assertEqual(ahorcado.vidas, vidas_actual - 1)
      
   def test_actualizar_estado_juego_y_ganar(self):
      ahorcado = Ahorcado("palabra")
      ahorcado.vidas = 6
      ahorcado.arriesgar_letra("p")
      ahorcado.arriesgar_letra("a")
      ahorcado.arriesgar_letra("l")
      ahorcado.arriesgar_letra("r")
      ahorcado.arriesgar_letra("b")
      ahorcado.actualizar_estado_juego()
      self.assertEqual(ahorcado.estado, ahorcado.ESTADOS["VICTORIA"])
   
   def test_actualizar_estado_juego_y_perder(self):
      ahorcado = Ahorcado("palabra")
      ahorcado.vidas = 6
      ahorcado.arriesgar_letra("z")
      ahorcado.arriesgar_letra("x")
      ahorcado.arriesgar_letra("o")
      ahorcado.arriesgar_letra("ñ")
      ahorcado.arriesgar_letra("w")
      ahorcado.arriesgar_letra("m")
      ahorcado.actualizar_estado_juego()
      self.assertEqual(ahorcado.estado, ahorcado.ESTADOS["DERROTA"])
   
if __name__ == '__main__':
    unittest.main()