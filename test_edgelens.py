# test_edgelens.py
"""
Tests for EdgeLens module.
"""

import unittest
from edgelens import EdgeLens

class TestEdgeLens(unittest.TestCase):
    """Test cases for EdgeLens class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EdgeLens()
        self.assertIsInstance(instance, EdgeLens)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EdgeLens()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
