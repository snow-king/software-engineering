import unittest
from Task_one.validation import validation


class TestValidation(unittest.TestCase):
    """ test for   """

    def setUp(self):
        self.password = validation("kawabanga!")

    def test_ideal(self):
        self.assertEqual(self.password.setInput("kawabanga!"), False)

    def test_wrong(self):
        self.assertEqual(self.password.setInput("sure?"), False)

    def test_empty(self):
        self.assertEqual(self.password.setInput(""), False)

    def test_drop(self):
        self.assertFalse(self.password.setInput("DROP TABLE USER"))


if __name__ == '__main__':
    unittest.main()
