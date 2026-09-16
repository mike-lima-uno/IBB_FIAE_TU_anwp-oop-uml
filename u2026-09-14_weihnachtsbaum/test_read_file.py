import tempfile
import unittest
from pathlib import Path

from read_file import read_trees_from_file


class ReadTreesFromFileTests(unittest.TestCase):
    def test_reads_generated_csv_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "christmas_trees.txt"
            file_path.write_text(
                "planting_date, height_m, diameter_m\n"
                "2024-01-14,1.23,1.08\n"
                "2023-12-01,2.5,1.7\n",
                encoding="utf-8",
            )

            trees = read_trees_from_file(str(file_path))

            self.assertEqual(len(trees), 2)
            self.assertEqual(trees[0]["Tree ID"], 1)
            self.assertEqual(trees[0]["Planting Date"], "2024-01-14")
            self.assertEqual(trees[0]["Height (m)"], 1.23)
            self.assertEqual(trees[0]["Diameter (m)"], 1.08)


if __name__ == "__main__":
    unittest.main()
