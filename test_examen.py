import unittest
import numpy as np
from examen_del_primer_parcial import (numero_de_matricula, capitalizacion, asistencia_dispersion,
                                       histograma_np, correlacion, probabilidad_condicional,
                                       problema_especifico, importancia, objetivos, tipo_de_datos
                                       )

class TestNumpyExercises(unittest.TestCase):

    def test_matricula(self):
        ''' Verifica número de matrícula'''
        self.assertEqual(numero_de_matricula in (173644, 179289, 175800, 178361, 177735,
                                       175056, 177156, 176308, 179598, 173577,
                                       175344, 178424, 172660, 178646, 177771,
                                       176635, 177488, 175596, 179287, 173846,
                                       174074, 175367, 171817),
                        True)
    
    def test_capitalizacion(self):
        result = capitalizacion()
        expected_result = (90.88888888888889,
                           79.0,
                          17,
                          61.81247196908899)
        self.assertAlmostEqual(result[0], expected_result[0], places=2)
        self.assertEqual(result[1], expected_result[1])
        self.assertEqual(result[2], expected_result[2])
        self.assertAlmostEqual(result[3], expected_result[3], places=2)

    def test_asistencia_dispersion(self):
        result = asistencia_dispersion()
        expected_result = (38200,
                          1182924100.0,
                          34401.04646876061)
        self.assertEqual(result[0], expected_result[0])
        self.assertAlmostEqual(result[1], expected_result[1], places=2)
        self.assertAlmostEqual(result[2], expected_result[2], places=2)

    def test_histograma_np(self):
        result = histograma_np()
        expected_result = (np.array([1, 1, 1, 3, 4, 5, 4, 3, 3, 2]),
                           np.array([4.8, 5.32, 5.84, 6.36, 6.88,
                                     7.4, 7.92, 8.44, 8.96, 9.48, 10.]))
        self.assertTrue(np.array_equal(result[0], expected_result[0]))
        self.assertTrue(np.allclose(result[1], expected_result[1]))

    def test_correlacion(self):
        result = correlacion()
        expected_result = 0.9847557478565358
        self.assertAlmostEqual(result,
                               expected_result,
                               places=2)

    def test_probabilidad_condicional(self):
        result = probabilidad_condicional()
        expected_result = (0.52,
                        0.46153846153846156)
        self.assertAlmostEqual(result[0],
                               expected_result[0],
                               places=2)
        self.assertAlmostEqual(result[1],
                               expected_result[1],
                               places=2)
        
    def test_proyecto(self):
        self.assertEqual(type(problema_especifico()), str)
        self.assertEqual(type(importancia()), str)
        self.assertEqual(type(objetivos()), str)
        self.assertEqual(type(tipo_de_datos()), str)



