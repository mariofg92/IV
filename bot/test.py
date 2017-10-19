#!/usr/bin/python
# -*- coding: utf-8 -*-

from funcionalidades import FuncionalidadDatos
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.actividad = FuncionalidadDatos()
        self.facultades = ("etsiit", "magisterio", "ciencias")
        self.tipos = ("charla", "taller", "curso")

    def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.actividad,FuncionalidadDatos, "Objeto creado correctamente")

    def test_consulta_correcta(self):
        self.assertIsInstance(self.actividad,FuncionalidadDatos, "El objeto es una actividad")

    def test_horas_OK(self):
        self.assertTrue(self.actividad.GetHoraI() != self.actividad.GetHoraF(), "La hora de comienzo e inicio no es la misma")

    def test_facultad_OK(self):
        self.assertTrue(self.actividad.GetFacultad() in self.facultades, "El campo facultad es un valor valido")

    def test_tipos_OK(self):
        self.assertTrue(self.actividad.GetTipo() in self.tipos, "El campo tipo es un valor valido")



if __name__ == '__main__':
     unittest.main()
