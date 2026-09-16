import pandas as pd
from pathlib import Path

#           _____________
#          |             |
#          |     file    |
#          |             |
#          |-------------|
#          |-------------|
#          |-------------|
#          |_____________|



def read_trees_from_file(filename):
    """Read Christmas tree data from a CSV file and print it."""
    
    script_directory = Path(__file__).resolve().parent
    output_file = script_directory / filename

    dataframe = pd.read_csv(output_file, encoding="utf-8")
    print(dataframe.to_string(index=False))
    return dataframe


if __name__ == "__main__":
    read_trees_from_file("christmas_trees.csv")
