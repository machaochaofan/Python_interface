import unittest


class Test3_3(unittest.TestCase):

    def test01(self):
        a = "上海"
        b = "yoyo"
        self.assertEqual(a, b, msg="失败")
if __name__ == '__main__':
    unittest.main()

