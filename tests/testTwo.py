import unittest
from Task_one.sum_and_multiplication import Num


class MyTestCase(unittest.TestCase):
    """ test for task 1.2  """

    # this method is loaded ahead of the tests
    def setUp(self):
        self.password = Num()

    # tests for sum
    def test_sum_ideal(self):
        self.password.getNumbers("1 2 3 4 5")
        self.assertEqual(self.password.sum(), 15)

    def test_sum_void(self):
        self.password.getNumbers(' ')
        self.assertEqual(self.password.sum(), 0)

    def test_sum_string(self):
        self.password.getNumbers('dev nul')
        self.assertRaises(TypeError, self.password.sum())

    # tests for multiply
    def test_multiply_ideal(self):
        self.password.getNumbers("1 2 3 4 5")
        self.assertEqual(self.password.multiplication(), 120)

    def test_multiply_void(self):
        with self.assertRaises(TypeError):
            self.password.getNumbers(' ')
            self.assertEqual(self.password.multiplication(), 0)

    def test_multiply_string(self):
        with self.assertRaises(TypeError):
            self.password.getNumbers('dev nul')
            self.assertEqual(TypeError, self.password.multiplication())


if __name__ == '__main__':
    unittest.main()
