from datetime import date, timedelta
import random

from pathlib import Path

#               *
#              /_\
#             /o o\
#            /_o_o_\
#           /o_o_o_o\
#          /_o_o_o_o_\
#         /o_o_o_o_o_o\
#        /_o_o_o_o_o_o_\
#              |||
#              |||
#           ___|||___
#          |_________|


def generate_christmas_trees(count=10):
    """Generate a list of Christmas trees with SI measurements."""

    random.seed(42)
    start_date = date(2015, 1, 1)
    trees = []

    for tree_id in range(1, count + 1):
        planting_date = start_date + timedelta(
            days=random.randint(0, 3650)
        )

        height_m = round(random.uniform(0.8, 3.5), 2)
        diameter_m = round(random.uniform(0.4, 2.0), 2)

        trees.append({
            "id": tree_id,
            "planting_date": planting_date.isoformat(),
            "height_m": height_m,
            "diameter_m": diameter_m
        })

    print(f"Generated {count} Christmas trees.")
    return trees


def generate_file(trees, filename="christmas_trees.csv"):
    """Save the tree list to a text file."""
    
    # Get current python directory and create file there
    script_directory = Path(__file__).resolve().parent
    output_file = script_directory / filename

    with output_file.open("w", encoding="utf-8") as file:
        file.write("planting_date, height_m, diameter_m\n")

        for tree in trees:
            file.write(
                f"{tree['planting_date']},{tree['height_m']},{tree['diameter_m']}\n"
            )

    print(f"File created at: {output_file.name}")

if __name__ == "__main__":
    christmas_trees = generate_christmas_trees()
    generate_file(christmas_trees)

    print("The file 'christmas_trees.csv' was created successfully.")
