import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """
        Set up a SimpleCalculator instance before each test.
        """
        self.calculator = SimpleCalculator()

    def test_add(self):
        """
        Test the add method with various cases.
        """
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(2.5, 3.5), 6.0)

    def test_subtract(self):
        """
        Test the subtract method with various cases.
        """
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(0, 5), -5)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(2.5, 1.5), 1.0)

    def test_multiply(self):
        """
        Test the multiply method with various cases.
        """
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 100), 0)
        self.assertEqual(self.calculator.multiply(2.5, 4), 10.0)

    def test_divide(self):
        """
        Test the divide method with various cases.
        """
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(-6, 3), -2)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(5, 0)
