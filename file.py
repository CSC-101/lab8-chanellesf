import sys
from typing import Optional

# Returns the float sum of two elements in a given list, converts the elements to float before computing
# INPUT: list with two elements of str
# OUTPUT: float sum
def str_to_float_sum(text : list[str]) -> Optional[float]:
    try:
        return float(text[0]) + float(text[1])
    except:
        print("An error occurred.")


def main():
    file_name = sys.argv[1]
    infile = open(file_name)
    count = 0
    with open(file_name, "r") as file:
        for line in infile:
            x = line.split()
            count += 1
            print("[LINE: ", count, "]: SUM =", str_to_float_sum(x))

try:
    main()
except FileNotFoundError:
    print("Error: file not found")