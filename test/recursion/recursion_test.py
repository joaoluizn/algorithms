from unittest import TestCase
from src.recursion.fibonacci import fibonacci

class FibonacciTest(TestCase):

    def test_fibonacci_of_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_of_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_of_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_of_3(self):
        self.assertEqual(fibonacci(3), 2)

    def test_fibonacci_of_4(self):
        self.assertEqual(fibonacci(4), 3)

    def test_fibonacci_of_5(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_of_6(self):
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_of_10(self):
        self.assertEqual(fibonacci(10), 55)
