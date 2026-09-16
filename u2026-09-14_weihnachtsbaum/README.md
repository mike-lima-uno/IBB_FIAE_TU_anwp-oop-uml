# Weihnachtsbaum

This project creates and reads Christmas tree data from a CSV file.

## Objective

The main idea is to generate tree data with:
- planting date
- height in meters
- diameter in meters

These data can then be read and displayed easily for analysis.

## pandas

The project uses pandas to simplify working with tables and CSV files.

Pandas offers several advantages:
- simple reading of CSV files
- organization of data in tables (DataFrame)
- fast selection and display of columns
- conversion and manipulation of values
- clear output in the terminal

This makes it easier than reading the file manually line by line, while allowing the data to be processed efficiently and clearly.

## Main files

- `create_file.py` — generates the tree data and saves it to the CSV file
- `read_file.py` — reads the CSV file with pandas and prints the data
- `main.py` — runs the main workflow of the project

## Execution

To run the project:

```bash
python [path_to_file\]main.py
```

This creates the CSV file and then reads it to display the results on the screen.
