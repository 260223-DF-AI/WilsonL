# HelloWorldTest.py
import unittest
from src.main.lab import Lab


class HelloWorldTest(unittest.TestCase):
    def setUp(self):
        self.hw = Lab()

    def test_hello(self):
        """
        Method sayHello() must return "Hello, World!". The strip method will remove any extra spaces or newlines at the end.
        """
        expected = "Hello, World!"
        actual = self.hw.sayHello().strip()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
