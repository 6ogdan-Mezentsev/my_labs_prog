import unittest
from src.lab1.calculator import function
class CalculatorTestCase(unittest.TestCase):


    def test_addition(self):
        (self.assertEqual(function.add(self,2, 3), 5))

    def test_sub(self):
        self.assertEqual(function.sub(self, 10, 3), 7)

    def test_multyplication(self):
        self.assertEqual(function.mult(self, 3, 9), 27)

    def test_divide(self):
        self.assertEqual(function.div(self,10,2), 5)




