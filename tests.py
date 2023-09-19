import unittest
from ahorcado import Ahorcado
class Test(unittest.TestCase):

   def test_letra_pertenece_y_adivinar(self):
      ahorcado = Ahorcado("palabra")
      self.assertTrue(ahorcado.letra_pertenece("b"))

   def test_letra_pertenece_y_errar(self):
      ahorcado = Ahorcado("palabra")
      self.assertFalse(ahorcado.letra_pertenece("e"))

   def test_arriesgar_letra_y_errar(self):
      ahorcado = Ahorcado("palabra")
      ahorcado.arriesgar_letra("e")
      self.assertEqual(ahorcado.estado, "_ _ _ _ _ _ _")
      
   def test_arriesgar_letra_unica_y_acertar(self):
      ahorcado = Ahorcado("palabra")
      ahorcado.arriesgar_letra("p")
      self.assertEqual(ahorcado.estado, "p _ _ _ _ _ _")
   
   def test_arriesgar_letra_multiple_y_acertar(self):
      ahorcado = Ahorcado("palabra")
      ahorcado.arriesgar_letra("a")
      self.assertEqual(ahorcado.estado, "_ a _ a _ _ a")

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
      ahorcado.restar_vidas()
      self.assertEqual(ahorcado.vidas, 5)
   
   
if __name__ == '__main__':
    unittest.main()