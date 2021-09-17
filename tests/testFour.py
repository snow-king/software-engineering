import random
import unittest
from Task_two.search import search


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.search_str = search()

    # check on lines where there are definitely no characters
    def test_dont_have_Yes(self):
        none = 'bcdefgjsp[uklmzc,l ;sv'
        for i in range(100):
            none_str = ''.join(random.choice(none) for i in range(10))
            self.search_str.getStr(none_str)
            self.assertEqual(self.search_str.seek_something(), "No")

    def test_one_match(self):
        test = ",.zncl,nzxljcl;jxaaz;lcnzxnm/kc;l'zj "
        self.search_str.getStr(test)
        self.assertEqual(self.search_str.seek_something(), "Yes")

    def test_all_match(self):
        test = "000zxcj;;qjsdjq;slkdaaaaz.,cmz.cxj;lzxj"
        self.search_str.getStr(test)
        self.assertEqual(self.search_str.seek_something(), "Yes")

    def test_void(self):
        with self.assertRaises(TypeError):
            self.search_str.getStr()
            self.assertEqual(self.search_str.seek_something(), "No")

    def test_void_str(self):
        self.search_str.getStr('')
        self.assertEqual(self.search_str.seek_something(), "No")


if __name__ == '__main__':
    unittest.main()
