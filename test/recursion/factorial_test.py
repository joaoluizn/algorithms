from unittest import TestCase
from src.recursion.factorial import factorial

class FactorialTest(TestCase):

    def test_fibonacci_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_fibonacci_of_1(self):
        self.assertEqual(factorial(1), 1)

    def test_fibonacci_of_2(self):
        self.assertEqual(factorial(2), 2)

    def test_fibonacci_of_3(self):
        self.assertEqual(factorial(3), 6)

    def test_fibonacci_of_4(self):
        self.assertEqual(factorial(4), 24)

    def test_fibonacci_of_10(self):
        self.assertEqual(factorial(10), 3628800)
