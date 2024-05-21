# tests/test_update_tutorial.py

import unittest
from api.create_tutorial import create_tutorial
from api.update_tutorial import update_tutorial

class TestUpdateTutorial(unittest.TestCase):
    def setUp(self):
        self.tutorial = create_tutorial("Test Tutorial", "Test Description", True)

    def test_update_tutorial(self):
        updated_tutorial = update_tutorial(self.tutorial['id'], description="Updated Description")
        self.assertIsNotNone(updated_tutorial)
        self.assertEqual(updated_tutorial['id'], self.tutorial['id'])
        self.assertEqual(updated_tutorial['description'], "Updated Description")
        self.assertEqual(updated_tutorial['title'], self.tutorial['title'])
        self.assertEqual(updated_tutorial['published'], self.tutorial['published'])
        self.assertIn('updatedAt', updated_tutorial)
        self.assertNotEqual(updated_tutorial['updatedAt'], self.tutorial['updatedAt'])

if __name__ == '__main__':
    unittest.main()
