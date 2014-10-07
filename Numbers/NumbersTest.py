from unittest import TestCase
from Numbers import Numbers
import unittest


class NumbersTest(TestCase):

    def test_init(self):
        num = Numbers(1, 2, 3)
        self.assertEqual(1, num.a, "A have wrong value. Actual result: " + str(num.a))
        self.assertEqual(2, num.b, "B have wrong value. Actual result: " + str(num.b))
        self.assertEqual(3, num.c, "C have wrong value. Actual result: " + str(num.c))

    def test_sum(self):
        num = Numbers(1, 2, 0)
        self.assertEqual(3, num.sum(), "Wrong sum. Actual result: " + str(num.sum()))

    def test_multiplication(self):
        num = Numbers(1, 2, 0)
        self.assertEqual(0, num.multiplication(), "Wrong multiplication. Actual result: " + str(num.multiplication()))

    def test_abs_multiplication(self):
        num = Numbers(1, -2, 1)
        self.assertEqual(2, num.abs_multiplication(),
                         "Wrong absolute multiplication. Actual result: " + str(num.abs_multiplication()))

if __name__ == '__main__':
    unittest.main()