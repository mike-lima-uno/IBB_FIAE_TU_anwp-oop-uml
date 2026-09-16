from create_file import generate_christmas_trees, generate_file
from read_file import read_trees_from_file

if __name__ == "__main__":
    filename = "christmas_trees.csv"
    nr_of_threes = 10

    christmas_trees = generate_christmas_trees(nr_of_threes)
    generate_file(christmas_trees, filename)

    read_trees_from_file(filename)
    print("done.")