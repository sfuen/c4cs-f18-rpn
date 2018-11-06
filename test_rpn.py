import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        stack = list()
        result = rpn.calculate("1 1 +", stack)
        self.assertEqual(2, result)
    def test_sub(self):
        stack = list()
        result = rpn.calculate("5 3 -", stack)
        self.assertEqual(2, result)
    def test_multiply(self):
        stack = list()
        result = rpn.calculate("5 3 *", stack)
        self.assertEqual(15, result)
    def test_divide(self):
        stack = list()
        result = rpn.calculate("6 3 /", stack)
        self.assertEqual(2, result)
    def test_exponent(self):
        stack = list()
        result = rpn.calculate("2 3 ^", stack)
        self.assertEqual(8, result)
    def test_persistence(self):
        stack = list()
        rpn.calculate("2 3 *", stack)
        rpn.calculate("1 1", stack)
        self.assertListEqual([6, 1, 1], stack)

if __name__ == '__main__':
    unittest.main()
