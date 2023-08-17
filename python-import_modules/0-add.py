#!/usr/bin/python3
"""This module imports the add function from add_0.py and prints the result of 1 + 2 = 3"""

# Import the add function from add_0.py
from add_0 import add

def main():
    # Assign values to variables a and b
    a = 1
    b = 2

    # Call the add function and print the result using string format
    print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    main()
