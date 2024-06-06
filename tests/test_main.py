# tests/test_main.py

import unittest
from src.main import greet

class TestGreet(unittest.TestCase):
    
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

if __name__ == '__main__':
    unittest.main()

