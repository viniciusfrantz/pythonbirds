import unittest

from oo.carro import Motor

class CarroTestCase(unittest.TestCase):
    def test_velocidade_inicial(self):
        motor= Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1,motor.velocidade)


