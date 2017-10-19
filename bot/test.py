from funcionalidades import FuncionalidadDatos
import unittest

class Test(unittest.TestCase):

     def setUp(self):
        self.actividad = FuncionalidadDatos()

     def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.actividad,FuncionalidadDatos, "Objeto creado correctamente")

     def test_consulta_correcta(self):
        self.assertIsInstance(self.actividad,FuncionalidadDatos, "El objeto es una actividad")

     def test_horas_correctas(self):
        self.assertTrue(self.actividad.ComprobarHoras, "La hora de comienzo e inicio no es la misma")



if __name__ == '__main__':
     unittest.main()
