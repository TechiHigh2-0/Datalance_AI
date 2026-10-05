import unittest
import pandas as pd
from src.statistics import generate_statistics
from src.visualizations import generate_auto_visualizations

class TestPhase3(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "A": [1, 2, 3, 4, 5],
            "B": ["apple", "banana", "apple", "cherry", "banana"],
            "C": [10.5, 20.1, 15.2, 5.0, 30.3]
        })
        
    def test_statistics(self):
        stats = generate_statistics(self.df)
        self.assertIn("numerical", stats)
        self.assertIn("categorical", stats)
        self.assertEqual(len(stats["numerical"]), 2) # A, C
        self.assertEqual(len(stats["categorical"]), 1) # B
        
    def test_visualizations(self):
        figs = generate_auto_visualizations(self.df)
        self.assertEqual(len(figs), 3) # 2 numerical histograms, 1 categorical bar chart

if __name__ == "__main__":
    unittest.main()
