import unittest
from random import randint
from Task_two.custom_math import Calculate


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_ideal(self):
        elements = [randint(-500, 500) for i in range(100)]
        for i in range(1, len(elements)):
            self.assertEqual(self.calc.difference(elements[i], elements[i - 1]), elements[i] - elements[i - 1])

    def test_void(self):
        with self.assertRaises(TypeError):
            self.calc.difference()

    def test_letter(self):
        self.assertRaises(TypeError, self.calc.difference("what", "?"))


if __name__ == '__main__':
    unittest.main()
