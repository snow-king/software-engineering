import unittest
from Task_one.validation import validation


class TestValidation(unittest.TestCase):
    """ test for task 1.1  """

    def setUp(self):
        self.password = validation("kawabanga!")

    def test_ideal(self):
        self.assertEqual(self.password.setInput("kawabanga!"), False)

    def test_wrong(self):
        self.assertEqual(self.password.setInput("sure?"), True)

    def test_empty(self):
        self.assertEqual(self.password.setInput(""), True)

    def test_drop(self):
        self.assertTrue(self.password.setInput("DROP TABLE USER"))


if __name__ == '__main__':
    unittest.main()
