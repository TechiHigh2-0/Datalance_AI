import unittest
import pandas as pd
from io import BytesIO
from src.data_loader import load_data
from src.profiler import profile_dataset

class MockUploadedFile(BytesIO):
    def __init__(self, name, content):
        super().__init__(content)
        self.name = name

class TestPhase2(unittest.TestCase):
    def test_csv_upload(self):
        csv_data = b"Date,Product,Sales,Region\n2023-01-01,A,100,N\n2023-01-02,A,100,N"
        mock_file = MockUploadedFile("test.csv", csv_data)
        df = load_data(mock_file)
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 2)
        
    def test_profiler(self):
        df = pd.DataFrame({
            "A": [1, 2, 2, None],
            "B": ["x", "y", "y", "z"]
        })
        profile = profile_dataset(df)
        self.assertEqual(profile["num_rows"], 4)
        self.assertEqual(profile["num_cols"], 2)
        self.assertEqual(profile["missing_values"]["A"], 1)
        self.assertEqual(profile["duplicate_rows"], 1)

if __name__ == "__main__":
    unittest.main()
