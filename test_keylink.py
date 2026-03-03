# test_keylink.py
"""
Tests for KeyLink module.
"""

import unittest
from keylink import KeyLink

class TestKeyLink(unittest.TestCase):
    """Test cases for KeyLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KeyLink()
        self.assertIsInstance(instance, KeyLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KeyLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
