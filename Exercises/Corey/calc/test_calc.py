import unittest
import Exercises.Corey.calc.calc as calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 10),20)
        self.assertEqual(calc.add(-5, 10), 5)
        self.assertEqual(calc.add(-5, -5), -10)
        self.assertEqual(calc.add(0,0), 0)

    def test_sub(self):
        result = calc.sub(10,10)
        self.assertEqual(result,0)

    def test_mult(self):
        result = calc.mult(10, 10)
        self.assertEqual(result, 100)

    def test_div(self):
        # result = calc.div(10, 0)
        # self.assertEqual(result, "Cannot divide by 0")
        self.assertRaises(ZeroDivisionError,calc.div,10,0)