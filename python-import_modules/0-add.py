#!/usr/bin/python3

# Using add_0 function from the add_0.py module
from add_0 import add

def main():
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    main()
