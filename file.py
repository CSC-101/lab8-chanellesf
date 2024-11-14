import sys
from typing import Optional


def str_to_float_sum(text : list[str]) -> Optional[float]:
    try:
        return float(text[0]) + float(text[1])
    except:
        print("An error occurred.")


def main():
    file_name = sys.argv[1]
    infile = open(file_name)
    count = 0
    for line in infile:
        x = line.split()
        count += 1
        print("[LINE: ", count, "]: SUM =", str_to_float_sum(x))

try:
    main()
except:
    print("Error: file not found")