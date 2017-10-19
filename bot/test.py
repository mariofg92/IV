from funcionalidades import FuncionalidadDatos
import unittest

class Test(unittest.TestCase):

     def setUp(self):
        self.actividad = FuncionalidadDatos()

     def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.actividad,FuncionalidadDatos, "Objeto creado correctamente")

if __name__ == '__main__':
     unittest.main()
