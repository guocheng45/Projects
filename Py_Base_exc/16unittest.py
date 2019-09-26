import unittest
import requests

class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这是测试整个类前要执行的方法")

    def setUp(self):
        print("这是每个测试方法前面运行的方法")

    def tearDown(self):
        print("这是每一个测试方法后面运行的方法")

    def test_first(self):
        print("这是第一个测试方法")
        res = requests.get('http://wwww.baidu.com')
        print(res.text)

    def test_second(self):
        print("这是第二个测试方法")
        res = requests.get('https://www.baidu.com/s?wd=python')
        print(res.text)

    @classmethod
    def tearDownClass(cls):
        print("这是测试整个类之后要执行的方法")

if __name__=='__main__':
    unittest.main()