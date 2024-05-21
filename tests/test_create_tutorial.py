# tests/test_create_tutorial.py

import unittest
from api.create_tutorial import create_tutorial

class TestCreateTutorial(unittest.TestCase):
    def test_create_tutorial(self):
        tutorial = create_tutorial("Test Tutorial", "Test Description", True)
        self.assertIsNotNone(tutorial)
        self.assertIn('id', tutorial)
        self.assertEqual(tutorial['title'], "Test Tutorial")
        self.assertEqual(tutorial['description'], "Test Description")
        self.assertEqual(tutorial['published'], 1)
        self.assertIn('createdAt', tutorial)
        self.assertIn('updatedAt', tutorial)

if __name__ == '__main__':
    unittest.main()
